from fastapi.responses import JSONResponse, FileResponse
from fastapi import Query,Path, APIRouter
from fastapi.responses import JSONResponse, FileResponse
from typing import List
from src.models.movie_model import Movie, MovieCreate,MovieUpdate

#Array
movies: List[Movie] = []
#Router
movie_router = APIRouter()




#CRUD
#CRUD
#CRUD
#CRUD

@movie_router.get('', tags=["Movies"], status_code=200)
def get_movies() -> List[Movie]:
    content = [movie.model_dump() for movie in movies] #Convertirlo a diccionario
    return JSONResponse(content=content)

#Parametros query
@movie_router.get('/by_category', tags=['Movies']) 
def get_movie_by_category(category:str = Query(min_length=5, max_length=20), year:int = Query(ge=1900)) -> Movie | dict:
    for movie in movies:
        if movie.category == category and movie.year == year:
            return JSONResponse(content = movie.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404) 

#Parametros de Ruta
@movie_router.get('/{id}', tags=["Movies"])
def get_movie_by_id(id:int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content= movie.model_dump(), status_code=200)
        return JSONResponse(content={}, status_code=404)

    


# @movie_router.post('/movies', tags=['Movies']) 
# def create_movie(id:int = Body() ,name:str = Body() ,year:int = Body() ,category:str = Body()):
#     movies.append({
#         'id':id,
#         'name':name,
#         'year':year,
#         'category':category, 
#     })
#     return movies 
#Post hacie el model

@movie_router.post('/', tags=['Movies'], status_code=200, response_description='Movie added') 
def create_movie(movie:MovieCreate) -> List[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies] #Convertirlo a diccionario
    return JSONResponse(content=content, status_code=200)
    #return RedirectResponse('/movies', status_code=303)


#Actualizar un registro 
@movie_router.put('/{id}', tags=['Movies']) 
def update_movie(id:int, movie:MovieUpdate) -> List[Movie]:
    for item in movies:
        if item.id==id:
            item.name = movie.name
            item.year = movie.year
            item.category = movie.category
    content = [movie.model_dump() for movie in movies] #Convertirlo a diccionario
    return JSONResponse(content = content, status_code=200)


#Borrar registro mediante ID
@movie_router.delete('/{id}', tags=['Movies'])
def del_movie(id:int)  -> List[Movie]:
    for item in movies: 
        if item.id==id:
            movies.remove(item)
    content = [movie.model_dump() for movie in movies] #Convertirlo a diccionario
    return JSONResponse(content=content, status_code=200)



# @movie_router.get('/get_file')
# def get_file():
#     return FileResponse('Archivo.pdf')
