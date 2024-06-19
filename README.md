# Library Management System Backend

This is the backend repository for the Library Management System, a web-based application for managing library resources, users, and transactions. The backend is built using Flask, a lightweight Python web framework, and provides a RESTful API for the frontend to interact with.

This project is an assignment for the course "Database Course Design". The front-end project address: https://github.com/larryyan/library-management-system-frontend"

## Features

- User authentication and authorization
- Book management (add, update, delete, search)
- User management (add, update, delete, search)
- Borrowing and returning books
- Overdue book tracking
- Reporting and statistics

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/larryyan/library-management-system-backend.git
   ```

2. Navigate to the project directory:

   ```
   cd library-management-system-backend
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```
   flask create
   ```

7. Start the development server:

   ```
   python app.py
   ```

   The backend server will be running at `http://localhost:5000`.

## API Endpoints

The following are the main API endpoints provided by the backend:

- `POST /login`: User login
- `POST /logout`: User logout
- `GET /books/<id>`: Get a specific book by ID
- `POST /books`: Add a new book
- `PUT /books/<id>`: Update a book
- `DELETE /books/<id>`: Delete a book
- `GET /book_info`: Get detailed information about all books
- `GET /book_info/<id>`: Get detailed information about a book
- `GET /reader/<id>`: Get a specific user by ID
- `POST /reader`: Add a new user
- `PUT /reader/<id>`: Update a user
- `DELETE /reader/<id>`: Delete a user
- `POST /borrow/<book_id>/<reader_id>`: Borrow a book
- `POST /return/<book_id>/<reader_id>`: Return a book

For detailed information about request and response formats, please refer to the API documentation.

## Database Schema

The backend uses SQLite as the database. The main tables in the database schema are:

- `reader`: Stores user information
- `book`: Stores book information
- `borrow`: Stores borrowing transactions
- `book_info`: Stores detailed information about books

For more details about the database schema, please refer to the database migration files in the `migrations` directory.


## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.