import json


class Io():


    def add_file_book(self,book):
        with open("books.json","a") as j:
            json.dump(book,j)


    def add_file_user(self,user):
        with open("users.json","a") as j:
            json.dump(user,j)


    def read_file_user(self):

        with open("users.json","r") as j:
            users = json.load(j)

        return users


    def read_file_book(self):

        with open("books.json","r") as j:
            books = json.load(j)

        return books


