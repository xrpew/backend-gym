from fastapi import FastAPI, Depends, Header, HTTPException
from database.db import fetch_all_data, insert_data
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")


def get_auth(x_token: str = Header(None)):
    if x_token == '1234':
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get('/')
async def root(auth: dict = Depends(get_auth)):
    if auth:
        data = fetch_all_data()
        for row in data:
            print(row)
        return JSONResponse(content={"message": "Users show on terminal"}, status_code=200)
        
    else:
        return 'Unauthorized'

@app.post('/')
async def add_user(name, age, plan, document, auth: dict = Depends(get_auth)):
    if auth:
        try:
            insert_data(name, age, plan, document)
            # Mostrar todos los registros para comprobar que el nuevo registro se añadió
            data = fetch_all_data()
            for row in data:
                print(row)
            return JSONResponse(content={"message": "User added correct"}, status_code=201)
        except:
            return JSONResponse(content={"error": "Error ocurred"}, status_code=400)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")