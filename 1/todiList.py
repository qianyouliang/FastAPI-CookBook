from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    task: str

todos = [{
    "id": 1,
    "task": "Learn FastAPI"
}]

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
def read_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    for todo in todos:
        print(todo),"todo"
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[i] = updated_todo
            return updated_todo
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo["id"]== todo_id:
            del todos[i]
            return {"message": "Todo deleted"}
    return {"error": "Todo not found"}

# 启动 FastAPI 应用程序的指令
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)