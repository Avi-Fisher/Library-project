from book.Book import Book
from user.User import User
from io1.Io import Io
from library.Library import Library


class Menu():

    def __init__(self):

        self.lib = Library()


    def load_library(self):

        load_lib = Io().load_library()
        books = load_lib["books"]
        users = load_lib["users"]

        for b in books:
            book = Book(b["title"],b["isbn"],b["author"],b["is_available"])

            self.lib.add_book(book)

        for u in users:
            user = User(u["name"],u["id"],u["borrowed_books"])

            self.lib.add_book(user)


    def save_library(self):
        Io().save_library(self.lib.books,self.lib.users)



















