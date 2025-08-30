import sqlite3

class Bookstore:
    def __init__(self):
        self.books = []
        self.total_sales = 0
        self.load_books_from_db()

    def load_books_from_db(self):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT, author TEXT, price REAL, isbn TEXT, number INTEGER)")
        conn.commit()
        cur.execute("SELECT * FROM books")
        self.books = cur.fetchall()
        conn.close()

    def add_book(self, name, author, price, isbn, number):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO books (name, author, price, isbn, number) VALUES (?, ?, ?, ?, ?)", (name, author, price, isbn, number))
        conn.commit()
        conn.close()
        self.load_books_from_db()

    def sell_book(self, name, author, number):
        self.load_books_from_db()
        for book in self.books:
            if book[1] == name and book[2] == author:
                if book[5] < number:
                    return "Not enough number of books available."
                total_price = number * book[3]
                self.total_sales += total_price
                new_number = book[5] - number
                self.update_book_number(book[0], new_number)
                return f"Total Price: ${total_price:.2f}"
        return "Book not found."

    def update_book_number(self, book_id, new_number):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("UPDATE books SET number=? WHERE id=?", (new_number, book_id))
        conn.commit()
        conn.close()

    def remove_book(self, book_id):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()
        conn.close()
        self.load_books_from_db()

    def search_book(self, name, author):
        result = []
        for book in self.books:
            if (name.lower() in book[1].lower() and author.lower() in book[2].lower()):
                result.append(book)
        return result

    def sales_report(self):
        return f"Total Sales: ${self.total_sales:.2f}"
