from fastapi import Depends, FastAPI
from typing import Optional

app = FastAPI()

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    return commons.__dict__

@app.get("/users/")
async def read_users(commons: CommonQueryParams = Depends(CommonQueryParams)):
    return commons.__dict__

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8009)