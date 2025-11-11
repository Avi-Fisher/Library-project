import json


class Io:


    def save_library(self,list_book,list_users):

        lib = {"books": [book.__dict__ for book in list_book], "users": [user.__dict__ for user in list_users]}

        with open("library.json","w") as j:
            json.dump(lib,j,indent = 4)



    def load_library(self):

        with open("library.json","r") as j:
            library = json.load(j)

        return library




