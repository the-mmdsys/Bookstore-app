from tkinter import Tk
from database import Bookstore
from gui import BookstoreApp

if __name__ == '__main__':
    root = Tk()
    bookstore = Bookstore()
    app = BookstoreApp(root, bookstore)
    root.mainloop()
