import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# 定义请求体模型
class Item(BaseModel):
    name: str

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return {"name": item.name}

if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)