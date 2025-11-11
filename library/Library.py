from book.Book import *
from user.User import *


class Library:
    def __init__(self):
        self.books = []
        self.users = []


    def add_book(self,book):
        for b in self.books:
            if b.title == book.title:
                return "This book is already exist"
        self.books.appand(book)
        print("Book is added successfully")



    def add_user(self, user):
        for u in self.users:
            if u.id == user.id:
                return "This user already exist!"
        self.users.append(user)
        print("User created successfully!")


    def find_book(self, book_isbn):
        for b in self.books:
            if b.isbn == book_isbn:
                return b
        return None

    def find_user(self,user_id):
        for u in self.users:
            if u.id == user_id:
                return u
        return None

    def borrow_book(self, user_id, book_isbn):
        book = self.find_book(book_isbn)
        user = self.find_user(user_id)
        if book != None:
            if user != None:
                if book.is_available == True:
                    user.borrowed_books.append(book)
                    book.is_available = False
                else:
                    return print("The book is not available")
            return print("Username not registered")
        else:
            return print("The book is not available in the library.")

    def return_book(self, user_id, book_isbn):
        book = self.find_book(book_isbn)
        user = self.find_user(user_id)
        if book != None:
            if user != None:
                if book.is_available == False:
                    user.borrowed_books.remove(book)
                    book.is_available = True
                else:
                    return print("The book has already been returned")
            return print("Username not registered")
        else:
            return print("The book is not available in the library.")


    def list_available_books(self):
        list_available = []
        for book in self.books:
            if book.is_available == True:
                list_available.append(book)
            else:
                pass
        return list_available

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return print("The book does not exist")









