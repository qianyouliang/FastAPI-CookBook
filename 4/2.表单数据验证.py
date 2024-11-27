from fastapi import FastAPI, Form, HTTPException
import uvicorn

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(min_length=4), password: str = Form(min_length=6)):
    """
    处理用户登录请求，验证 username 和 password 的长度
    """
    return {"username": username}


if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)