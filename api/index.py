from fastapi import FastAPI, Query
from duckduckgo_search import ddg

app = FastAPI()

@app.get('/search')
async def search(q: str = Query(..., description='Keywords to search'), max_results: int = Query(3, description='Maximum number of results')):
    print(q)
    results = ddg(q, region='wt-wt', max_results=max_results)
    return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port='8000')
    app.run(host='0.0.0.0')