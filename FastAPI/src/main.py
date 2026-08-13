import os
from fastapi import FastAPI, Query, Request, Response, status, Depends
from fastapi.responses import  JSONResponse, PlainTextResponse
from src.routers.movie_router import movie_router
from src.utilis.http_error_handler import HTTP_error_handler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
app.add_middleware(HTTP_error_handler) 
static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

app.mount('/static', StaticFiles(directory=static_path), name = 'static ')

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



# def commonParams(startDate:str, endDate:str ):
#     return {'startDate': startDate, 'endDate': endDate }

# commonsParm = Annotated[dict, Depends(commonParams)]

class CommonsParams:
    def __init__(self, startDate:str, endDate:str ):
        self.startDate = startDate 
        self.endDate = endDate 


@app.get('/users', tags=["Users"])
def get_users(commons:CommonsParams = Depends(CommonsParams)):
    return f'User created from {commons.startDate} to {commons.endDate}'


@app.get('/customers', tags=["Users"])
def get_customers(commons:CommonsParams = Depends(CommonsParams)):
    return f'customers created from {commons.startDate} to {commons.endDate}'

