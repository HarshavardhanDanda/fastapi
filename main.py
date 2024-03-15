from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="This is my first rote")
async def root():
    return {"message": "Hello World"}