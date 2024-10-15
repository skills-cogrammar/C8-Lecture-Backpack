'''
Using the Book class we created in Week 5's Task Walkthrough, do the following:

1. Populate a list with elements of the Book class
2. Append a book to the list and swap the positions of items in the list
3. Extend one list that contains objects of the Book class with more Book objects 
   from another list
4. Sort according to number of copies available, using the key parameter and creating 
   a lambda function to access copy numbers
5. Find a book within the list and using the enumerate function to retrieve the 
   position of this book after ranking according to number of copies
'''

class Book: # defining a Book class to be the blueprint
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    # Method to check if copy is available
    def copy_in_library(self):
        return self.copies > 0 # Return True if there is at least 1 copy, False otherwise


# 1. Populate a list with elements of the Book class

library = [
    Book("1984", "George Orwell", 4),
    Book("Long Walk to Freedom", "Nelson Mandela", 15),
    Book("The Power of Mental Disciple", "Alec Zeit", 24)
]

# 2. Append a book to the list and swap the positions of items on the list
library.append(Book("Alice in Wonderland", "Lewis Carrol", 0))

library[0], library[3] = library[3], library[0]

# 3. Extend one list that contains objects of the Book class with more Book objects from another list

more_books = [Book("The Room on the Roof", "Ruskin Bond", 37)]
library.extend(more_books)

# 4. Sort according to number of copies available, using the key parameter and creating a lambda function to access copy numbers

library.sort(key = lambda book: book.copies)

# 5. Find a book within the list and using the enumerate function to retrieve the position of this book after ranking according to number of copies

book_to_find = "The Room on the Roof"

for i, book in enumerate(library):
    if book.title == book_to_find:
        print(f"The book {book_to_find} is in position {i}.")