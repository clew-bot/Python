print("First Python Program")

"""
We will be going over the basics of Python in this course. We will be using Python 3.6.1.
"""

# This is a comment. Comments are used to explain code. They are not run by the interpreter.

# This is a print statement. It prints out a string to the console.
print("Hello World")

# This is a variable. Variables are used to store data. They are created on the fly.
# You do not need to declare a variable before using it.
my_variable = 10

# This is a function. Functions are used to group code that is used multiple times.
# They are also used to group code that is used to perform a specific task.
def my_function():
    print("Hello from a function")

# This is a class. Classes are used to group data and functions that are used together.
# They are also used to create objects.
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
        
# This is an object. Objects are created from classes. They are used to access data and functions that belong to a class.
my_object = MyClass()

print(my_object.variable) # This will print out "blah".

my_object.function() # This will print out "This is a message inside the class."

# This is a conditional statement. It is used to check for certain conditions and perform a task based on the condition.
if 1 == 1:
    print("1 and 1 are equal")

# This is a loop. It is used to repeat a task multiple times.
for i in range(1, 10):
    print(i) # This will print out the numbers 1 - 9

# This is a library. Libraries are used to add additional functionality to Python.
# They are imported into your code using the import statement.
import random

# This is a list. Lists are used to store multiple items in a single variable.
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list[0]) # This will print out "1"
print(my_list[1]) # This will print out "2"
print(my_list[2]) # This will print out "3"
