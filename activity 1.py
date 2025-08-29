# Base class
class Book:
    def __init__(self, title, author, dds_number):
        self.title = title
        self.author = author
        self.dds_number = dds_number   # Dewey Decimal Number
    
    def info(self):
        print(f"'{self.title}' by {self.author}, DDS: {self.dds_number}")

    def read(self):
        print(f"Reading '{self.title}' 📖")


# Derived class
class Ebook(Book):
    def __init__(self, title, author, dds_number, file_size):
        super().__init__(title, author, dds_number)
        self.file_size = file_size
    
    # Polymorphism: overriding info()
    def info(self):
        print(f"Ebook: '{self.title}' by {self.author}, File size: {self.file_size}MB, DDS: {self.dds_number}")

    def download(self):
        print(f"Downloading '{self.title}'... 💾")


# Create objects
book1 = Book("Things Fall Apart", "Chinua Achebe", "896")
ebook1 = Ebook("Digital Librarianship", "Smith Johnson", "025", 5)

# Using methods
book1.info()
book1.read()

ebook1.info()
ebook1.download()
