'''
Concepts that need to be understood:
1. Classes and Objects
2. Attributes and Methods
3. Inheritance and Method Overriding
4. Conditional Logic for Object Instantiation
'''

'''
Classes and Objects 
Create a class called Developer that initialises name and language attributes and 
has a method called introduce() that prints out the developer's name and programming 
language.
'''

class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def introduce(self):
        print(f"My name is {self.name} and I code in {self.language}.")

# Create an instance of Developer and use introduce() method on it
dev_1 = Developer("Amen", "Python")
dev_1.introduce()

'''
INHERITANCE
Create a parent class for an online course which initialises the 
course title and course duration attributes. Include a 
course_info() method in this class that prints out these details.
'''

class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def course_info(self):
        print(f"Course: {self.title}, Duration: {self.duration} hours.")

'''
Create a child class called CodingCourse which inherits from 
Course. Within this child class, call the parent class constructor 
and initialise the language attribute. Include a method called 
course_language() that prints out the programming language.
'''

class CodingCourse(Course):
    def __init__(self, title, duration, language):
        super().__init__(title, duration)
        self.language = language
    
    def course_language(self):
        print(f"Programming language: {self.language}.")

'''
Finally, use the relevant methods on this child class to print
out the course information and programming language used.
'''

coding_course_1 = CodingCourse("Introduction to Programming", 2, "Python")
coding_course_1.course_info()
coding_course_1.course_language()

'''
METHOD OVERRIDING
Create a parent class for software licenses that includes a terms 
method which prints out that the license is for general use. Create
a child class of the License called OpenSourceLicense that overrides
the terms method and prints out that the software is open-source.
Create another child class called ProprietaryLicense that overrides 
the terms method and prints out that the software can not be 
redistributed.
'''

class License:
    def terms(self):
        print("This software is for general use.")

class OpenSourceLicense(License):
    def terms(self):
        print("This software is open source.")

class ProprietaryLicense(License):
    def terms(self):
        print("This software is proprietary and cannot be redistributed.")

'''
Ask the user if the online resource is free of copyright. Given their input, 
create the appropriate object and call on the terms method to give the user
appropriate feedback.
'''

user_input = input("Is the software free of copyright? Enter Y/N.")

if user_input == 'Y':
    license_type = OpenSourceLicense()
    license_type.terms()

elif user_input == 'N':
    license_type = ProprietaryLicense()
    license_type.terms()

else:
    print("Invalid input.")