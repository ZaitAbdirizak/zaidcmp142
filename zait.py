#this project is for Library management system

class Book:
  def __init__(self, title, author):
    self.title = "python guide"
    self.author = "jake"

f1 = Books()
f1.title = "python guide"
f1.author = "jake"
print(f1.title)
print(f1.author)

#using single inheritance

class Library:
  def open(self):
    print("Library open")

#child class Book inheritsthe base class Library

class Book(Library):
  def available(self):
    print("Book available")

d = Book()
d.available()
d.open()


#using multiple inheritance

class Bookshelf1:
  def Addition(self, x, y):
    return x + y;

class Bookshelf2:
  def Multiplication(self, x, y):
    return x * y;

class Library(Bookshelf1, Bookshelf2):
  def Subtraction(self, x, y):
    return x - y;

d = Subtraction()
print(d.Adition (10, 8))
print(d.Multiplication (4, 6))
print(d.Subtraction (7, 2)
      
      


#Multi level inheritance

class Library:
  def Open(self):
    print("Library open")

#The child class shelf inherits the base class Library

class Shelf(Library):
  def Clean(self):
    print("Shelves are clean")

#the child class books inherits another child class Shelf

class Books(Shelf):
  def Arrange(self):
    print("Books are arranged")

d = Books()
d.Open()
d.Clean()
d.Arrange()


    



