# How to populate a dictionary
dictionary = {}

dictionary['Birthday'] = '09/01/2015'
dictionary['Name'] = "Sally"
dictionary['Age'] = 19

# print(dictionary.items())

class Book: # defining a Book class to be the blueprint
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    # Method to check if copy is available
    def copy_in_library(self):
        return self.copies > 0 # Return True if there is at least 1 copy, False otherwise
    
library = {}

library["Atomic Habits"] = Book("Atomic Habits","James Clear", 2)
library["Brave New World"] = Book("Brave New World", "Aldous Huxley", 1)
library["The Twilight Saga"] = Book("The Twilight Saga", "Stephenie Meyer", 0)

'''
This is what the library dictionary looks like: 

library = {
    "Atomic Habits" : Book("Atomic Habits","James Clear", 2),
    "Brave New World" : Book("Brave New World", "Aldous Huxley", 1),
    "The Twilight Saga" : Book("The Twilight Saga", "Stephenie Meyer", 0)
}

'''

print(library.items())