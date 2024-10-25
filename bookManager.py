import sqlite3

con = sqlite3.connect("books.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, year INTEGER, copy_count INTEGER)")

def check_id_exists(id):
    cur.execute("SELECT id FROM books WHERE id=?", (id,))
    existing_book = cur.fetchone()
    if existing_book:
        return True
    else:
        return False

def create_book(id, title, author, genre, year, copy_count):
    if check_id_exists(id):
        print("Book ID already exists in the database.")
    else:
        cur.execute("INSERT INTO books (id=?, title=?, author=?, genre=?, year=?, copy_count)=?",
                    (id, title, author, genre, year, copy_count))
        con.commit()
        print(f"Book with ID of {id} created.")

def read_all_books():
    cur.execute("SELECT * FROM books")
    return cur.fetchall()

def read_book(id):
    if check_id_exists(id):
        cur.execute("SELECT * FROM books WHERE id=?", (id,))
        return cur.fetchone()
    else:
        return "Book not found"

def update_book(id, title, author, genre, year, rating):
    if check_id_exists(id):
        cur.execute("UPDATE books SET title=?, author=?, genre=?, year=?, rating=? WHERE id=?",
                    (title, author, genre, year, rating, id))
        con.commit()
        return f"Book with ID of {id} updated."
    else:
        return "Book not found"

def delete_book(id):
    if check_id_exists(id):
        cur.execute("DELETE FROM books WHERE id=?", (id,))
        con.commit()
        return f"Book with ID of {id} deleted."
    else:
        return "Book not found"
    
print(delete_book(5))