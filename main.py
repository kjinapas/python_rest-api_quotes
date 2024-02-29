from fastapi import FastAPI
from pydantic import BaseModel
from routers import quotes_api,appgame
app = FastAPI()

app.include_router(quotes_api.router)
app.include_router(appgame.router)

def Hello():
    print("hello world")
@app.get("/")

async def root():
    Hello()
    return {"message": "Hello World"}

