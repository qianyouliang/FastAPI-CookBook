import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义基础模型
class BaseItem(BaseModel):
    description: str
    type: str

# 定义 CarItem 模型，继承自 BaseItem
class CarItem(BaseItem):
    type: str = "car"

# 定义 PlaneItem 模型，继承自 BaseItem
class PlaneItem(BaseItem):
    type: str = "plane"
    size: int

# 示例数据
items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

# 定义路由，使用 Union 类型作为响应模型
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]

# 启动 FastAPI 应用
if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)