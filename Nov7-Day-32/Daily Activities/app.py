from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import json
import os
from dotenv import load_dotenv
import httpx
from fastapi.responses import HTMLResponse

load_dotenv()

app = FastAPI()

# Use environment variable for OpenRouter API key and endpoint
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"  # verify actual URL

class Prompt(BaseModel):
    query: str

    @validator('query')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Query cannot be empty")
        return v

def save_qa_history(question, answer):
    file = "qa-history.json"
    history = []
    if os.path.exists(file):
        with open(file, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    history.append({"question": question, "answer": answer})
    with open(file, "w") as f:
        json.dump(history, f, indent=2)

@app.post("/generate")
async def generate_response(prompt: Prompt):
    if not prompt.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",  # replace with your actual model id on OpenRouter
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt.query}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OPENROUTER_API_URL, headers=headers, json=data)
        if response.status_code != 200:
            detail = response.text
            raise HTTPException(status_code=500, detail=f"OpenRouter API error: {detail}")
        result = response.json()
        answer = result.get('choices', [{}])[0].get('message', {}).get('content', '')

    save_qa_history(prompt.query, answer)
    return {"response": answer}

@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>AI Knowledge Assistant</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 10px; background: #f0f4f8; }
        h1 { text-align: center; color: #333; }
        textarea { width: 100%; height: 80px; padding: 10px; font-size: 16px; }
        button { background: #007bff; color: white; border: none; padding: 12px 20px; font-size: 16px; cursor: pointer; }
        button:hover { background: #0056b3; }
        #response { margin-top: 20px; padding: 15px; background: white; border-radius: 8px; min-height: 80px; white-space: pre-wrap; }
        .error { color: red; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Ask a Question</h1>
    <textarea id="query" placeholder="Type your question here..."></textarea><br/>
    <button onclick="sendQuestion()">Ask</button>
    <div id="response"></div>
    <div id="error" class="error"></div>

    <script>
        async function sendQuestion() {
            document.getElementById("error").textContent = "";
            let query = document.getElementById("query").value.trim();
            if (!query) {
                document.getElementById("error").textContent = "Question cannot be empty.";
                return;
            }
            document.getElementById("response").textContent = "Loading...";
            try {
                let res = await fetch("/generate", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({query})
                });
                let data = await res.json();
                if (res.ok) {
                    document.getElementById("response").textContent = data.response;
                } else {
                    document.getElementById("response").textContent = "";
                    document.getElementById("error").textContent = data.detail || data.error || "Error occurred";
                }
            } catch (e) {
                document.getElementById("response").textContent = "";
                document.getElementById("error").textContent = "Network error";
            }
        }
    </script>
</body>
</html>
"""
