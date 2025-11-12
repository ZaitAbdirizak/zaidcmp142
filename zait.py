#this project is for Library management system

class Book:
  def __init__(self, title, author):
    self.title = "python guide"
    self.author = "jake"

f1 = Book()
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


#using Method overlording (compile-time polymorphism)

class libraryweb:
  def Register(self, name):
    print(f'Registered librarian: {name}")


  def Register(self, name, book):
    print(f"Registered librarian: {name} for book: {book}")


  def Register(self, name, book, date):
    print(f"Registered librarian: {name} for {book} in date {date}")

library = libraryweb()
library.register("jake", "game of thrones", "12")

    

    



