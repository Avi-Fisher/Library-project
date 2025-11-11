
class User:

    def __init__(self,name,id,borrowed_books = []):

        self.name= name
        self.id = id
        self.borrowed_books = borrowed_books


    def __str__(self):

        return f"Name: {self.name}, Id: {self.id}, Borrowed books: {self.borrowed_books}"



