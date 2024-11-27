from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def get_default():
    return {"message": "Hello, World!"}
    

# 示例 1：获取特定用户的信息
@app.get("/users/{user_id}")
def get_user(user_id: int):
    # 假设我们从数据库中获取用户信息
    user_info = {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
    return user_info

# 示例 2：获取特定用户的订单
@app.get("/users/{user_id}/orders/{order_id}")
def get_order(user_id: int, order_id: int):
    # 假设我们从数据库中获取订单信息
    order_info = {"user_id": user_id, "order_id": order_id, "product": "Laptop", "price": 1200}
    return order_info

# 示例 3：更新特定用户的订单
@app.put("/users/{user_id}/orders/{order_id}")
def update_order(user_id: int, order_id: int, new_product: str, new_price: float):
    # 假设我们更新数据库中的订单信息
    if not order_exists(user_id, order_id):
        raise HTTPException(status_code=404, detail="Order not found")
    
    # 更新订单信息
    update_order_in_db(user_id, order_id, new_product, new_price)
    
    return {"message": "Order updated successfully"}

def order_exists(user_id: int, order_id: int) -> bool:
    # 假设我们检查订单是否存在
    return True  # 示例中假设订单总是存在

def update_order_in_db(user_id: int, order_id: int, new_product: str, new_price: float):
    # 假设我们更新数据库中的订单信息
    pass

# 启动 FastAPI 应用程序的指令
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)