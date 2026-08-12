import os
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import  JSONResponse, PlainTextResponse
from src.routers.movie_router import movie_router
from src.utilis.http_error_handler import HTTP_error_handler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.add_middleware(HTTP_error_handler) 
static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

app.mount('/static', StaticFiles(directory=static_path), name = 'static')

templates = Jinja2Templates(directory=templates_path, )

#middleware desde FastAPI
# app.add_middleware('http')
# async def HTTP_error_handler(request, call_next) -> Response | JSONResponse:
#         try:
#             return await call_next(Request)
#         except Exception as e:
#             return JSONResponse(content=f'{e}', status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

        
@app.get('/', tags=["Home"])
def home(request:Request):
    return templates.TemplateResponse(  
        request=request,
        name='index.html',
        context={'message': 'Hola'})

app.include_router(prefix='/movie', router=movie_router)

