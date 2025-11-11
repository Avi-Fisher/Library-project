

from book.Book import Book
from user.User import User
from library.Library import Library
from io1.Io import Io

class Menu:



    def __init__(self):

        self.library = Library()



    def load_library(self):
        try:
            load_lib = Io().load_library()
        except:
            pass
        try:
            books = load_lib["books"]
            for b in books:
                book = Book(b["title"], b["isbn"], b["author"], b["is_available"])

                self.library.add_book(book)
        except:
            pass

        try:
            users = load_lib["users"]
            for u in users:
                user = User(u["name"], u["id"], u["borrowed_books"])

                self.library.add_book(user)
        except:
            pass

    def save_library(self):
        Io().save_library(self.library.books, self.library.users)



    def start(self):
        print("- - - - - - - - - - - - -")
        print("Welcome to the library")
        print("- - - - - - - - - - - - -")



    def manu(self):
        while True:
            print(""""
            ---
            MENU
            ---
            Add Book: 1
            Add User: 2
            Borrow Book: 3
            Return Book: 4
            List available books: 5
            Search book: 6
            Exit: 7
            """)

            choice = input("Please enter your choice: ")

            if choice == "1":
                title = input("Enter title: ")
                isbn = input("Enter isbn: ")
                author = input("Enter author: ")
                book = Book(title, isbn, author)
                self.library.add_book(book)

            elif choice == "2":
                name = input("Enter name: ")
                id = input("Enter id: ")
                user = User(name, id)
                self.library.add_user(user)

            elif choice == "3":
                user_id = input("Enter your id: ")
                book_isbn = input("Enter book isbn: ")
                self.library.borrow_book(user_id, book_isbn)

            elif choice == "4":
                user_id = input("Enter your id: ")
                book_isbn = input("Enter book isbn: ")
                self.library.return_book(user_id, book_isbn)

            elif choice == "5":
                self.library.list_available_books()

            elif choice == "6":
                title_book = input("Enter title: ")
                print(self.library.search_book(title_book))

            elif choice == "7":
                print("Thank you for visiting us. We would love to see you again.")
                self.save_library()

                break

            else:
                print("Invalid choice, try again.")




