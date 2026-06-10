from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="FastAPI Book Catalog")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    available: bool = True


books = [
    Book(id=1, title="FastAPI in Action", author="Example Author", year=2024),
]


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Book Catalog"}


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(book: Book):
    # Add the new book to the catalog.
    # Make sure the id is unique before saving it.
    books.append(book)
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # Find the book, replace it, and return the updated record.
    raise HTTPException(status_code=501, detail="Update book not implemented")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # Remove the matching book from the catalog.
    raise HTTPException(status_code=501, detail="Delete book not implemented")
