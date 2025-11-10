from encodings.punycode import selective_find


class User():

    def __init__(self,name,id):

        self.name= name
        self.id = id
        self.borrowed_books = []


    def __str__(self):

        return f"Name: {self.name}, Id: {self.id}, Borrowed books: {self.borrowed_books}"



