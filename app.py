from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import requests

ROOT_URL = "https://jsonplaceholder.typicode.com/todos"
OPENAPI_VERSION = "3.0.2"
app = FastAPI()
app.openapi_version = OPENAPI_VERSION

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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Todo API",
        version=OPENAPI_VERSION,
        description="Awesome app that gets todos.",
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://png.pngtree.com/png-vector/20190930/ourmid/pngtree-to-do-list-icon-cartoon-style-png-image_1768114.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
