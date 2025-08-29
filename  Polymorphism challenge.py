class Book:
    def read(self):
        print("Reading a generic book...")

class Ebook(Book):
    def read(self):
        print("Reading an Ebook on a tablet 📱")

class PrintedBook(Book):
    def read(self):
        print("Reading a printed book with fresh paper smell 📖")

class AudioBook(Book):
    def read(self):
        print("Listening to an audiobook 🎧")


# Demonstrating Polymorphism
books = [Ebook(), PrintedBook(), AudioBook()]

for b in books:
    b.read()
