#HEADERS
#Una petecion HTTP contienen informacion que esta relacionada con el contexto de la peticion
#contenido tipo hacia el server, info acerca del navegador, datos del user

from fastapi import FastAPI, HTTPException, Header, Depends
from typing import Annotated
app = FastAPI()


def get_headers(access_token: Annotated[str, Header()], 
                user_role:    Annotated[str, Header()]):

    if access_token != 'secret_token':
        raise HTTPException(status_code=401, detail='Unauthorized')
    return {'access_token':access_token, 'user_role':user_role,  }

@app.get('/dashboard')
def get_dashboard(headers: Annotated[dict, Depends(get_headers)]):

    return {'access_token': headers['access_token'], 'user_role': headers['user_role']}