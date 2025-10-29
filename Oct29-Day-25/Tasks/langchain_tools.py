# ============================================================
# Memory-Tools.py — Conversational Mistral Agent (with all tools)
# ============================================================

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")


# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.4,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)


# ------------------------------------------------------------
# 3. Define helper tools
# ------------------------------------------------------------

def summarize(text: str) -> str:
    """Summarize a long passage or conversation history."""
    prompt = f"Please summarize the following passage:\n\n{text}\n\nSummary:"
    try:
        response = llm.invoke(prompt)
        return f"Agent: {response.content}"
    except Exception as e:
        return f"Agent: Could not summarize the text. Error: {e}"


def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment of a text (positive, neutral, negative)."""
    prompt = f"Please analyze the sentiment of the following text:\n\n{text}\n\nSentiment:"
    try:
        response = llm.invoke(prompt)
        return f"Agent: {response.content}"
    except Exception as e:
        return f"Agent: Could not analyze the sentiment. Error: {e}"


# NoteKeeper: Simple memory store and retrieve system
#notes = []


# def add_note(note: str) -> str:
#     """Store a personal note."""
#     notes.append(note)
#     return f"Agent: Noted: \"{note}\""
#
#
# def get_notes() -> str:
#     """Retrieve stored personal notes."""
#     if not notes:
#         return "Agent: You have no notes stored."
#     return f"Agent: You currently have {len(notes)} note(s):\n" + "\n".join(notes)

# NoteKeeper: Simple memory store and retrieve system
notes = []

def add_note(note: str) -> str:
    """Store a personal note, preventing duplicates."""
    if note in notes:
        return f"Agent: The note \"{note}\" already exists."
    notes.append(note)
    return f"Agent: Noted: \"{note}\""

def get_notes() -> str:
    """Retrieve stored personal notes."""
    if not notes:
        return "Agent: You have no notes stored."
    return f"Agent: You currently have {len(notes)} note(s):\n" + "\n".join(notes)



def improve_text(text: str) -> str:
    """Improve the clarity and professionalism of text."""
    prompt = f"Rewrite the following text to make it clearer and more professional:\n\n{text}\n\nImproved Text:"
    try:
        response = llm.invoke(prompt)
        return f"Agent: {response.content}"
    except Exception as e:
        return f"Agent: Could not improve the text. Error: {e}"


def classify_priority(task: str) -> str:
    """Classify task priority (high, medium, low)."""
    high_keywords = ["urgent", "asap", "tonight", "immediately"]
    medium_keywords = ["by the end of the week", "soon", "this month"]
    low_keywords = ["when you have time", "sometime", "later"]

    # Check for priority based on keywords
    task_lower = task.lower()

    if any(keyword in task_lower for keyword in high_keywords):
        return f"Agent: Task \"{task}\" marked as HIGH priority."
    elif any(keyword in task_lower for keyword in medium_keywords):
        return f"Agent: Task \"{task}\" marked as MEDIUM priority."
    else:
        return f"Agent: Task \"{task}\" marked as LOW priority."


# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Handle Summarize command
    if user_input.lower().startswith("summarize"):
        text = " ".join(user_input.split()[1:]).strip()
        if not text:
            print("Agent: Please provide text to summarize. Example: summarize The meeting discussed cloud migration, database cleanup, and scaling.")
            continue
        print(summarize(text))
        memory.save_context({"input": user_input}, {"output": summarize(text)})
        continue

    # Handle Sentiment Analyzer command
    if user_input.lower().startswith("analyze"):
        text = " ".join(user_input.split()[1:]).strip()
        if not text:
            print("Agent: Please provide text to analyze. Example: analyze I feel frustrated about work today.")
            continue
        print(analyze_sentiment(text))
        memory.save_context({"input": user_input}, {"output": analyze_sentiment(text)})
        continue

    # Handle NoteKeeper command
    if user_input.lower().startswith("note"):
        note = " ".join(user_input.split()[1:]).strip()
        if not note:
            print("Agent: Please provide a note to remember. Example: note Remember to email the project report tomorrow.")
            continue
        print(add_note(note))
        memory.save_context({"input": user_input}, {"output": add_note(note)})
        continue

    if user_input.lower() == "get notes":
        print(get_notes())
        memory.save_context({"input": user_input}, {"output": get_notes()})
        continue

    # Handle Text Improver command
    if user_input.lower().startswith("improve"):
        text = " ".join(user_input.split()[1:]).strip()
        if not text:
            print("Agent: Please provide text to improve. Example: improve This report is kind of messy and confusing.")
            continue
        print(improve_text(text))
        memory.save_context({"input": user_input}, {"output": improve_text(text)})
        continue

    # Handle Task Priority Classifier command
    if user_input.lower().startswith("priority"):
        task = " ".join(user_input.split()[1:]).strip()
        if not task:
            print("Agent: Please provide a task to classify. Example: priority Submit proposal by tonight.")
            continue
        print(classify_priority(task))
        memory.save_context({"input": user_input}, {"output": classify_priority(task)})
        continue

    # Default: use LLM for other queries
    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)
