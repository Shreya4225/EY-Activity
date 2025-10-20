from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/sync-task")
def sync_task():
    time.sleep(10)
    return {"message": "sync task completed after 5 seconds"}

@app.get("/async-task")
async def sync_task():
    await asyncio.sleep(10)
    return {"message": "async task completed after 5 seconds"}