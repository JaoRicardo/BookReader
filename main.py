from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel

class Dado(BaseModel):
    valor:int

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

armazem = None

@app.get("/")
async def initial():
    return {"message": "Hello Word"}

#rota para listar os livros que estão na pasta epuv
@app.get("/api/books")
async def listBooks():
    books_files = [file for file in os.listdir("ebooks") if file.endswith(".epub")] # retorna só os arquivos que são epubs
    return books_files

# Roda que envia o arquivo referente ao nome do livro
@app.get("/api/books/{livro_id}", response_class=FileResponse)
async def showBook(livro_id:str):
    livro = livro_id
    caminhoLivro = os.path.join("ebooks", f"{livro}")
    return caminhoLivro

@app.post("/recebe")
async def recebePost(dado:Dado):
    global armazem
    armazem = dado

@app.get("/envia")
async def enviaGet():
    global armazem
    return armazem