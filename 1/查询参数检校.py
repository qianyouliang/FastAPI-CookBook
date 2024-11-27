from fastapi import FastAPI, Query

app = FastAPI()

# 1. 字符串参数限制
@app.get("/items/")
def read_items(q: str = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 2. 增加额外的约束条件
@app.get("/items_with_constraints/")
def read_items_with_constraints(
    q: str = Query(None, min_length=3, max_length=50, regex="^[a-z]+$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 3. 最短字符长度与正则表达式
@app.get("/items_with_regex/")
def read_items_with_regex(
    q: str = Query(None, min_length=3, max_length=50, regex="^[a-z]+$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 4. 声明必需参数与省略号
@app.get("/items_required/")
def read_items_required(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 5. 声明更多元数据
@app.get("/items_with_metadata/")
def read_items_with_metadata(
    q: str = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)