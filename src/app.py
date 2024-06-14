from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from .shared import Config
from .routes import routes

config = Config()

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

app.include_router(routes)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config['port'])