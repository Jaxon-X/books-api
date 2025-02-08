# Books API 📚

A simple CRUD API for managing books, built with Django and Django REST Framework.

## Installation  
```bash
git clone <repo-url>
cd books-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


API Endpoints
Method	URL	Description
GET	/books/	Retrieve all books
POST	/books/	Add a new book
GET	/books/id/	Get a single book
PUT	/books/id/	Update a book
DELETE	/books/id/	Delete a book
