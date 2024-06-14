from fastapi import Request
from fastapi.responses import JSONResponse
import traceback
from src.models import PyDexError

async def error_handling_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except PyDexError as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.message}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "detail": str(e),
                "traceback": traceback.format_exc()
            }
        )
