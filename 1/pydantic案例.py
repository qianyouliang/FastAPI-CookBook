from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError

app = FastAPI()

# 定义数据模型
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# 示例 1：创建新商品
@app.post("/items/")
def create_item(item: Item):
    # 数据已经通过 Pydantic 验证
    return {"message": "Item created successfully", "item": item}

# 示例 2：更新商品信息
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # 假设我们更新数据库中的商品信息
    if not item_exists(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    
    # 更新商品信息
    update_item_in_db(item_id, item)
    
    return {"message": "Item updated successfully", "item": item}

def item_exists(item_id: int) -> bool:
    # 假设我们检查商品是否存在
    return True  # 示例中假设商品总是存在

def update_item_in_db(item_id: int, item: Item):
    # 假设我们更新数据库中的商品信息
    pass

# 启动 FastAPI 应用程序的指令
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)