# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API with FastAPI and practice defining routes, request and response models, and common CRUD operations. You will create an in-memory book catalog that supports creating, reading, updating, and deleting records.

## 📝 Tasks

### 🛠️ Create the API Skeleton

#### Description
Set up a FastAPI application for a book catalog and implement the basic read endpoints.

#### Requirements
Completed program should:

- Create a FastAPI app instance and a root route that returns a welcome message.
- Define a Pydantic model for a book with fields such as `id`, `title`, `author`, and `year`.
- Implement a route that returns all books in the catalog.
- Implement a route that returns a single book by its ID.

### 🛠️ Add CRUD Operations and Validation

#### Description
Extend the API so users can add, update, and remove books while handling invalid requests cleanly.

#### Requirements
Completed program should:

- Implement a `POST /books` route that adds a new book to the catalog.
- Implement a `PUT /books/{book_id}` route that updates an existing book.
- Implement a `DELETE /books/{book_id}` route that removes a book.
- Return a `404` error when a requested book does not exist.
- Use FastAPI's automatic documentation at `/docs` to inspect and test the API.
