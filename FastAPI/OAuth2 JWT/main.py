from fastapi import FastAPI, Depends
from fastapi .security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from jose import jwt

#OAuth2 → DEFINE COMO EL CLIENTE OBTIENE EL TOKEN
#JWT → ES EL FORMATO DEL ACCESS TOKEN QUE EMITE LA API
#FastAPI → valida el JWT en cada request protegida.
#Refresh token → permite obtener nuevos access tokens sin volver a pedir usuario/contraseña.

#OAuth2PasswordBearer:  Es un flujo de autenticacion que utiliza un token, 
                    #.  Se crea apartir de una contraseña
app =FastAPI()
#El endpoint para obtener el token OAuth2 está en /token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users={
    "kike":{    
        'username':'kike', 
        'email':'kike@gmail.com', 
        'password':'123'
        },
    "juan":{
        'username':'juan', 
        'email':'juan@gmail.com', 
        'password':'123'}
}

#Genera el token apartir de info del user
def encode_token(payload: dict) -> str: #Regresa un string 
    #Recibe 3 parametros# dict con datos que generan el token, 
                        # clave secreta
                        # Algoritmo que se utilizara
    token = jwt.encode(payload, "my-secret", algorithm='HS256')
    return token

#Devuelve la informacion del user a la que pertenece ese token
def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict: #Regresa un dic 
    data = jwt.decode(token, 'my-secret', algorithms=['HS256'])
    user = users.get(data['username']) #Usuario al que pertence ese token
    return user



@app.post('/token')
#OAuth2PasswordRequestForm: Recibe diferentes valores, sirve para obtener usr y pass como formdata
def login(formData: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(formData.username)
    if not user or formData.password != user['password']:
        raise HTTPException(status_code=400, detail='User not found' )
    #Genera el token apartir del username y del email
    token = encode_token({'username':user['username'], 'email':user['email'] })
    return {'access_token': token}


@app.get('/users/profile')
def get_user(user: Annotated[dict, Depends(decode_token)]):
    return user 