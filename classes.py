### This file illustrates Python's implementation of classes and OOP

def sum(self, x, y):
    return x+y

# define a class
class AlgoPractice:
    # Encapsulation doesn't really exist. It is by convention if needed
    #
    # in python attributes are always public
    # can use __ to declare private as a convention (not enforced by interpreter)
    # interpreter replaces with _classname__attr (name mangling)
    
    # all methods in Python are VIRTUAL (can be overriden)

    # when a class method in Python is called
    # what actually happens is 
    # x.f() ==> MyClass.f(x)


    my_class_var = 'Class variables in Python are like static variables in Java'

    # functions outside of a class can be used as data attributes
    sum_func = sum

    # Constructor
    def __init__(self) -> None:
        # instance variables are bound to a specific object
        self.data = []
    
    def add(self, x):
        self.data.append(x)


class DoubleAdder(AlgoPractice):
    # this method calls parent class method add
    def add(self, x):
        AlgoPractice.add(x)
        AlgoPractice.add(x)


# We can add iterator behavior to any class
class Reverse:
    """Interator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    

def iter_demo():
    rev = Reverse("spam")
    iter(rev)
    for char in rev:
        print(char)

iter_demo()

print()

# alternative approach to class iterators
# Generators!
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

def generator_demo():
    for char in reverse('golf'):
        print(char)

generator_demo()