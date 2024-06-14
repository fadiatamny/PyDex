from dotenv import load_dotenv

from src.middlewares import error_handling_middleware
load_dotenv()

from fastapi import FastAPI
from src.shared import Config
from src.routes import routes

app = FastAPI()


app.middleware("http")(error_handling_middleware)


@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

app.include_router(routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=Config['port'])