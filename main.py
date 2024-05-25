from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from .shared import Config

config = Config()

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config['port'])