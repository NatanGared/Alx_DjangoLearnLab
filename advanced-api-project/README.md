# Advanced API Project

## Overview
This project implements a RESTful API for managing books using Django REST Framework.

## Endpoints
- **GET /api/books/**: List all books.
- **GET /api/books/<id>/**: Retrieve a single book.
- **POST /api/books/create/**: Create a new book (authenticated users only).
- **PUT /api/books/update/<id>/**: Update an existing book (authenticated users only).
- **DELETE /api/books/delete/<id>/**: Delete a book (authenticated users only).

## Permissions
- List and detail views are accessible to unauthenticated users.
- Create, update, and delete views require authentication.

# Advanced API Project

## API Features
### Filtering
- Filter books by title, author, and published date.

### Searching
- Search books by title or author.

### Ordering
- Order results by title or published date.

## Example Requests
- List books by title: `GET /api/books/?title=Harry Potter`
- Search for books: `GET /api/books/?search=Harry`
- Order books by published date: `GET /api/books/?ordering=published_date`