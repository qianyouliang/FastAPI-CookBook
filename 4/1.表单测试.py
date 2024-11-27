from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    """
    处理用户登录请求，接收表单字段 username 和 password
    """
    return {"username": username}



if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)