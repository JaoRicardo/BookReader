from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

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

@app.get("/")
async def initial():
    return {"message": "Hello Word"}

#rota para listar os livros que estão na pasta epuv
@app.get("/api/books")
async def listBooks():
    books_files = [file for file in os.listdir("ebooks") if file.endswith(".epub")] # retorna só os arquivos que são epubs
    return books_files

@app.get("/api/books/{livro_id}", response_class=FileResponse)
async def showBook(livro_id:str):
    livro = livro_id
    caminhoLivro = os.path.join("ebooks", f"{livro}")
    return caminhoLivro