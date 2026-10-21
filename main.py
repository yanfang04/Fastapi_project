from fastapi import FastAPI,Path
from routers import news
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# 注册路由
app.include_router(news.router)
