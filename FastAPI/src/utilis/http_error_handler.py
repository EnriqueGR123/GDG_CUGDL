from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request

class HTTP_error_handler(BaseHTTPMiddleware):
    def __init__(self, app:FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next)-> Response | JSONResponse:
        try:
            return await call_next(Request)
        except Exception as e:
            return JSONResponse(content=f'{e}', status_code = status.HTTP_500_INTERNAL_SERVER_ERROR) 