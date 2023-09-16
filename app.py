from fastapi import FastAPI
import requests

app = FastAPI()
ROOT_URL = "https://jsonplaceholder.typicode.com/todos"

@app.get("/health")
def health() -> dict:
    return {"message": "healthy"}

@app.get("/todos")
def todos() -> dict:
    res = requests.get(ROOT_URL).json()
    return {"data": res}

@app.get("/todos/{todo_id}")
def todo(todo_id: int) -> dict:
    res = requests.get(f"{ROOT_URL}/{todo_id}").json()
    return {"data": res}
