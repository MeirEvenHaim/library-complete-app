# Flask Library Management System

This Flask application serves as a simple Library Management System (LMS) that allows users to manage clients, books, and loans. It provides basic CRUD (Create, Read, Update, Delete) operations through a SQLite database backend.

## Steps to Create the Application

### Step 1: Setting Up the Project

1. **Initialize Flask App**

   - Create a new directory for your project.
   - Inside the project directory, create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

2. **Install Flask and SQLite**
   - Install Flask using pip:
     ```bash
     pip install Flask
     ```

### Step 2: Database Setup

1. **Define Database Schema**

   - Create a SQLite database `database.db`.
   - Define the following tables in `database.db`:
     - `clients`: Stores client information (`id`, `name`, `email`).
     - `books`: Stores book information (`id`, `title`, `author`).
     - `loans`: Stores loan information (`id`, `client_id`, `book_id`, `loan_date`, `return_date`).

2. **Create Tables**
   - Implement a function to create tables if they do not exist in the database. This function should be executed when the Flask app starts.

### Step 3: Implement Flask Routes

1. **Basic Routes**

   - Create routes for:
     - `/`: Home page.
     - `/manage_clients`: Manage clients (CRUD operations).
     - `/books`: Manage books (CRUD operations).
     - `/loans`: Manage loans (CRUD operations).

2. **Client Routes**

   - Implement CRUD operations for clients:
     - `GET /manage_clients`: Display all clients.
     - `POST /manage_clients`: Add a new client.
     - `PUT /clients/<id>`: Update a client.
     - `DELETE /clients/<id>`: Delete a client.

3. **Book Routes**

   - Implement CRUD operations for books:
     - `GET /books`: Display all books.
     - `POST /books`: Add a new book.
     - `PUT /books/<id>`: Update a book.
     - `DELETE /books/<id>`: Delete a book.

4. **Loan Routes**
   - Implement CRUD operations for loans:
     - `GET /loans`: Display all loans (including client and book information).
     - `POST /loans`: Add a new loan.
     - `PUT /loans/<id>`: Update a loan.
     - `DELETE /loans/<id>`: Delete a loan.

### Step 4: Frontend Integration

1. **Create Templates**

   - Develop HTML templates using Jinja2 for:
     - `index.html`: Main dashboard.
     - `manage_clients.html`: Client management interface.
     - `manage_books.html`: Book management interface.
     - `manage_loans.html`: Loan management interface.

2. **Style with CSS**
   - Create a `style.css` file to apply styles to HTML templates for a consistent look and feel.

### Step 5: Testing and Running the Application

1. **Run the Flask Application**

   - Start the Flask development server:
     ```bash
     python app.py
     ```
   - Access the application in a web browser at `http://localhost:5000`.

2. **Test Functionality**
   - Test CRUD operations for clients, books, and loans to ensure proper functionality.

## Functionality

- **Clients Management**:

  - Add, update, delete clients.
  - View list of clients.

- **Books Management**:

  - Add, update, delete books.
  - View list of books.

- **Loans Management**:
  - Add, update, delete loans.
  - View list of loans with associated client and book details.
