import uvicorn
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=5)]
):
    results = {"item_id": item_id}
    return results

@app.get("/items-float/{item_id}")
async def read_items(
    item_id: Annotated[float, Path(title="The ID of the item to get", ge=5.5)]
):
    results = {"item_id": item_id}
    return results


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8009)



