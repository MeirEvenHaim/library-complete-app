from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to establish SQLite connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create tables if they do not exist
def create_tables():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS clients
                   (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS books
                   (id INTEGER PRIMARY KEY, title TEXT, author TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS loans
                   (id INTEGER PRIMARY KEY, client_id INTEGER, book_id INTEGER,
                    loan_date TEXT, return_date TEXT, 
                    FOREIGN KEY(client_id) REFERENCES clients(id),
                    FOREIGN KEY(book_id) REFERENCES books(id))''')
    conn.commit()
    conn.close()

create_tables()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to manage clients
@app.route('/manage_clients', methods=['GET'])
def manage_clients():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()  # Fetch all clients from database
        conn.close()
        return render_template('manage_clients.html', clients=clients)  # Pass clients data to template
    except Exception as e:
        return str(e), 400

# Route to create a new client
@app.route('/clients', methods=['POST'])
def create_client():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_clients'))  # Redirect to manage clients page after successful creation
    except Exception as e:
        return str(e), 400

# Route to update a client
@app.route('/clients/<int:id>/update', methods=['POST'])
def update_client(id):
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE clients SET name = ?, email = ? WHERE id = ?", (name, email, id))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_clients'))  # Redirect to manage clients page after successful update
    except Exception as e:
        return str(e), 400

# Route to delete a client
@app.route('/clients/<int:id>/delete', methods=['POST'])
def delete_client(id):
    try:
        if request.method == 'POST':
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?", (id,))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_clients'))  # Redirect to manage clients page after successful deletion
    except Exception as e:
        return str(e), 400

# Route to manage books
@app.route('/manage_books', methods=['GET'])
def manage_books():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()  # Fetch all books from database
        conn.close()
        return render_template('manage_books.html', books=books)  # Pass books data to template
    except Exception as e:
        return str(e), 400

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    try:
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_books'))  # Redirect to manage books page after successful creation
    except Exception as e:
        return str(e), 400

# Route to update a book
@app.route('/books/<int:id>/update', methods=['POST'])
def update_book(id):
    try:
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, id))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_books'))  # Redirect to manage books page after successful update
    except Exception as e:
        return str(e), 400

# Route to delete a book
@app.route('/books/<int:id>/delete', methods=['POST'])
def delete_book(id):
    try:
        if request.method == 'POST':
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (id,))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_books'))  # Redirect to manage books page after successful deletion
    except Exception as e:
        return str(e), 400

# Route to manage loans
@app.route('/manage_loans', methods=['GET'])
def manage_loans():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT loans.id, clients.name AS client_name, books.title AS book_title, loans.loan_date, loans.return_date \
                        FROM loans \
                        INNER JOIN clients ON loans.client_id = clients.id \
                        INNER JOIN books ON loans.book_id = books.id")
        loans = cursor.fetchall()  # Fetch all loans from database
        conn.close()
        return render_template('manage_loans.html', loans=loans)  # Pass loans data to template
    except Exception as e:
        return str(e), 400

# Route to create a new loan
@app.route('/loans', methods=['POST'])
def create_loan():
    try:
        if request.method == 'POST':
            client_id = request.form['client_id']
            book_id = request.form['book_id']
            loan_date = request.form['loan_date']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO loans (client_id, book_id, loan_date) VALUES (?, ?, ?)",
                           (client_id, book_id, loan_date))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_loans'))  # Redirect to manage loans page after successful creation
    except Exception as e:
        return str(e), 400

# Route to update a loan
@app.route('/loans/<int:id>/update', methods=['POST'])
def update_loan(id):
    try:
        if request.method == 'POST':
            client_id = request.form['client_id']
            book_id = request.form['book_id']
            loan_date = request.form['loan_date']
            return_date = request.form['return_date']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE loans SET client_id = ?, book_id = ?, loan_date = ?, return_date = ? WHERE id = ?",
                           (client_id, book_id, loan_date, return_date, id))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_loans'))  # Redirect to manage loans page after successful update
    except Exception as e:
        return str(e), 400

# Route to delete a loan
@app.route('/loans/<int:id>/delete', methods=['POST'])
def delete_loan(id):
    try:
        if request.method == 'POST':
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM loans WHERE id = ?", (id,))
            conn.commit()
            conn.close()
            return redirect(url_for('manage_loans'))  # Redirect to manage loans page after successful deletion
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)
