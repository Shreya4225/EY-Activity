from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Bookstore(BaseModel):
    id: int
    title: str
    author: str
    price: float
    in_stock: bool

books = [
    {"id": 1, "title": "python1", "author": "anushka", "price": "500", "in_stock": True},
    {"id": 2, "title": "computer2", "author": "prajakta", "price": "600", "in_stock": False},
    {"id": 3, "title": "java3", "author": "shreya", "price": "800", "in_stock": True},
]

@app.get("/books")
def get_books():
    return {"books" : books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@app.post (path= "/books" , status_code=201)
def create_book(book: Bookstore):
    books.append(book.dict())
    return {"message":"book added successfully","book" : book}

@app.put("/books/{book_id}")
def updated_book(book_id: int, book: Bookstore):
    for i, s in enumerate(books):
        if s["id"] == book_id:
            books[i] = book.dict()
            return {"message": "book updated successfully", "book": books[i]}
    raise HTTPException(status_code=404, detail="book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, s in enumerate(books):
        if s["id"] == book_id:
            books.pop(i)
            return {"message": "book deleted successfully", "book": books[i]}
    raise HTTPException(status_code=404, detail="book not found")


@app.get("/books/search/author", response_model=List[Bookstore])
def search_by_author(author: Optional[str] = Query(None)):
    if not author:
        raise HTTPException(status_code=400, detail="Author query parameter is required.")

    results = [book for book in books if book["author"].lower() == author.lower()]
    if not results:
        raise HTTPException(status_code=404, detail="No books found for the given author.")

    return results

