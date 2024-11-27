from fastapi import FastAPI, UploadFile, HTTPException
import uvicorn

app = FastAPI()

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    """
    处理多文件上传请求，返回上传文件的详细信息列表
    """
    uploaded_files_info = []
    
    for file in files:
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
        
        # 添加文件的详细信息到列表中
        uploaded_files_info.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "size_in_bytes": content_bytes,
            "size_in_chars": content_chars,
            "file_content_info": file_content_info
        })
    
    # 返回所有上传文件的详细信息
    return {"uploaded_files_info": uploaded_files_info}

if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用
    uvicorn.run(app, host='127.0.0.1', port=8009)