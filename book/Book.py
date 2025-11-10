
class Book():

    def __init__(self):
        self.name = None
        self.type = None
        self.author = None
        self.book = None



    def creat_book(self):

        self.name = input("enter name book")
        self.type = input("enter type book")
        self.author = input("enter author book")

        self.book = {"name":self.name,"type":self.type,"author":self.author}












