
class Book():

    def __init__(self,title,author,ISBN,is_available = True):
        self.title = title
        self.isbn = ISBN
        self.author = author
        self.is_available = is_available



    def __str__(self):

       return f"Title: {self.title}, ISDN: {self.isbn}, Author: {self.author}, Is available: {self.is_available}"












