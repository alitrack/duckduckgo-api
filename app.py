# from flask import Flask, request
# from api.index import search
# app = Flask(__name__)


# app.route('/search')(search)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
from fastapi import FastAPI
from api.index import search

app = FastAPI()

@app.get('/search')
async def search_route(q: str, max_results: int = 3):
    return await search(q, max_results)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
