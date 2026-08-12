import datetime
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id:int
    name:str
    year:int
    category:str

class MovieCreate(BaseModel):
    #AÑADIR VALIDACIONES
    # GT mayor que # GE Mayor o igual, # LT menor que # LE menor o igual
    id:int 
    name:str = Field(min_length=5, max_length= 15)#default='')
    year:int = Field(le=datetime.date.today().year, ge=1900 )
    category:str = Field(min_length=5, max_length=100)
    #Se pueden utilizar en vez de los parametros, valores por defecto
    # model_config ={
    #     'json_schema_extra':{
    #         'example':{
    #             'id':1,
    #             'name':'Movie',
    #             'year':2020,
    #             'category':'accion',
    #         }
    #     }
    # }

    #VALIDAR UTILIZANDO VALIDATOR

    # @validator('title')
    # def validate_title(cls, value):
    #     if len(value) < 5:
    #         raise ValueError('Debe de ser mayor a 5 caracteres ')
    #     return super().validate(value)

class MovieUpdate(BaseModel):
    name:str
    year:int
    category:str
    model_config ={
        'json_schema_extra':{
            'example':{
                'name':'Movie',
                'year':2020,
                'category':'accion',
            }
        }
    }

