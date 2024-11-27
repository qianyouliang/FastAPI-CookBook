from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/upload/")
async def upload_file_and_form(
    file: UploadFile = File(None),  # 可选文件上传
    token: str = Form(...),  # 必填表单字段
    username: str = Form(min_length=4),  # 表单字段，最小长度为4
    password: str = Form(min_length=6)  # 表单字段，最小长度为6
):
    """
    处理文件和表单字段上传请求，返回文件名和表单字段值
    """
    # 检查文件是否为空
    if file is None or file.filename == "":
        return JSONResponse(content={"message": "No upload file sent"}, status_code=200)
    
    try:
        # 读取文件内容
        contents = await file.read()
        
        # 统计文件内容的字节数
        content_bytes = len(contents)
        
        # 尝试解码文件内容为字符串，并统计字符数
        try:
            content_chars = len(contents.decode('utf-8'))
        except UnicodeDecodeError:
            content_chars = None
        
        # 检查文件类型
        if file.content_type.startswith("image/"):
            file_content_info = "Binary image content"
        elif content_chars is not None:
            file_content_info = contents.decode('utf-8')
        else:
            file_content_info = "Binary content"
        
        # 返回文件和表单字段的详细信息
        return {
            "token": token,
            "username": username,
            "password": password,
            "filename": file.filename,
            "content_type": file.content_type,
            "size_in_bytes": content_bytes,
            "size_in_chars": content_chars,
            "file_content_info": file_content_info
        }
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail="Error processing file")

if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)