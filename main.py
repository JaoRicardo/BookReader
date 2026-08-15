from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def initial():
    return {"message": "Hello Word"}


@app.get("/api/books")
async def listBooks():
    books = os.listdir("ebooks")
    books_files = [file for file in os.listdir("ebooks") if file.endswith(".epub")]
    return books_files