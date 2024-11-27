from fastapi import FastAPI, UploadFile, HTTPException
import uvicorn

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """
    处理文件上传请求，验证文件类型并返回上传文件的详细信息
    """
    # 验证文件类型
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
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
    
    # 返回文件的详细信息
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_in_bytes": content_bytes,
        "size_in_chars": content_chars,
        "file_content_info": file_content_info
    }

if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)