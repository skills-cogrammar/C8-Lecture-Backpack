# Special Methods
# ================= __init__ and adding string representation.
class Student:
    def __init__(self, name, surname, age) -> None:
        """Initialise the student with a name, surname, and age."""
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"Fullname: {self.name} {self.surname}\nAge: {self.age}"

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f"Student({self.name!r}, {self.surname!r}, {self.age!r})"


# Example usage
student1 = Student("Alice", "Smith", 20)

# Demonstrating __str__ output (for users)
print(student1)  # Output: Fullname: Alice Smith, Age: 20

# Demonstrating __repr__ output (for developers)
print(repr(student1))  # Output: Student('Alice', 'Smith', 20)

# Adding student to a list (shows __repr__ in lists)
students = [student1]
print(students)  # Output: [Student('Alice', 'Smith', 20)]


# ================= Operator Overloading
class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    """
    When defining methods like __add__, __sub__, or similar,
    self refers to the instance the method is called on,
    and *others refer to the objects from the second one involved in the operation.
    """
    def __add__(self, *others):

        new_length = self.length
        new_width = self.width

        # Iterate over all additional Rectangle objects
        for other in others:
            new_length += other.length
            new_width += other.width

        return Rectangle(new_length, new_width)

    def __sub__(self, *others):
        new_length = self.length
        new_width = self.width

        # Iterate over all additional Rectangle objects
        for other in others:
            new_length -= other.length
            new_width -= other.width

        if new_length < 0: new_length = 0
        if new_width < 0: new_width = 0

        return Rectangle(new_length, new_width)

    def __str__(self) -> str:
        return f"Length: {self.length}\nWidth {self.width}"


# Demonstration
rect1 = Rectangle(5, 7)
rect2 = Rectangle(4, 9)
rect3 = Rectangle(2, 3)

# Both the below addition code options will work
rect_sum = rect1 + rect2 + rect3
# rect_sum = rect1.__add__(rect2, rect3)

print(rect_sum)


# ================= Container-like behaviour.
class BookShelf:

    def __init__(self, shelf_num, shelf_genre) -> None:
        """Initialise the bookshelf with a number, genre, and an empty list of books."""
        self.shelf_num = shelf_num
        self.shelf_genre = shelf_genre
        self.books = []

    def __getitem__(self, key):
        """Allow books to be accessed by index, like shelf[0]."""
        return self.books[key]

    def __len__(self):
        """Return the number of books on the shelf using len(shelf)."""
        return len(self.books)

    def __contains__(self, item):
        """Check if a specific book is on the shelf using 'in' keyword."""
        return item in self.books

    def __repr__(self) -> str:
        """Return a string representation of the bookshelf for developers."""
        return (f"BookShelf(shelf_num={self.shelf_num!r}, "
                f"shelf_genre={self.shelf_genre!r}, books={self.books})")


# Example usage
shelf = BookShelf(1, "Dystopian Fiction")

# Adding books directly to the list for simplicity
shelf.books.extend(["1984", "Brave New World", "Fahrenheit 451"])

# Accessing books using __getitem__
print(shelf[0])  # Output: 1984

# Checking the number of books using __len__
print(len(shelf))  # Output: 3

# Checking if a book is on the shelf using __contains__
print("Brave New World" in shelf)  # Output: True

# Printing the current state of the bookshelf
print(shelf)  
# Output: BookShelf(shelf_num=1, shelf_genre='Dystopian Fiction', books=['1984', 'Brave New World', 'Fahrenheit 451'])

# ================= Polymorphism
# print() is an examples of polymorphism as it does not care about
# the type of object it is receiving.
print("Hello")
print(3.14)
print(100)
print(True)


# ================= Implementing polymorphism using method overriding.
# Let's go back to our animals and see what polymorphism means.
class Animal:
    def __init__(self, sound: str) -> None:
        """Initialise the animal with a sound it makes."""
        self.sound = sound

    def make_sound(self) -> str:
        """The default make_sound method for the Animal class."""
        return f"The animal makes a {self.sound} sound."


class Lion(Animal):
    def __init__(self) -> None:
        super().__init__("rawr")

    def make_sound(self) -> str:
        return f"The fierce lion let's out a big {self.sound}!!!!!!"


class Canary(Animal):
    def __init__(self) -> None:
        super().__init__("tweet")

    def make_sound(self) -> str:
        sound = "The canary tries to impress his partner with a song from the soul."
        sound += f"{self.sound} {self.sound} {self.sound}."
        return sound


class Goldfish(Animal):
    def __init__(self) -> None:
        super().__init__("blub")

    def make_sound(self) -> str:
        return f"{self.sound} {self.sound}...................  {self.sound}"


# Pay attention to the return values of all the make_sound() functions
# Let's create a function that will make use of this behaviour.
def sound(sound_object):
    print(sound_object.make_sound())


# With all our make_sound funtions returning the same value none of them
# will break our function when passed as an argument.
animals = [Lion(), Canary(), Goldfish()]
for animal in animals:
    sound(animal)


# What if we don't return the correct value type.
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("woof")

    def make_sound(self) -> None:
        print(f"{self.sound} {self.sound} {self.sound}")


dog = Dog()
sound(dog)


# The above output "woof woof woof" comes from the print statement in
# make_sound and since nothing was returned from the make_sound method,
# the sound function has nothing to print and therefor prints None

# ================= Duck typing
# If it walks like a duck, swims like a duck and quacks like a duck
# then it might just be a duck.
class Dog():
    def __init__(self, sound) -> None:
        self.sound = sound

    def make_sound(self) -> None:
        return f"{self.sound} {self.sound} {self.sound}"


class Student:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def make_sound(self):
        return f"Hi, I'm {self.name} {self.surname}. I am {self.age} years old!"


def sound(sound_object):
    print(sound_object.make_sound())


"""
Here, we define a Dog and a Student class with a method make_sound(), which
returns a string. The classes themselves are not explicitly tied to any other
class or interface, and it doesn't need to inherit from a specific base class
for the purpose of "making sound."

Duck Typing focuses on the presence of methods or properties, allowing objects
to be used interchangeably based on behaviour rather than class inheritance.

The function sound() can be used here for different objects and different outcomes.
"""
student = Student("Jack", "Sparrow", 38)
sound(student)

dog = Dog("Woof")
sound(dog)
