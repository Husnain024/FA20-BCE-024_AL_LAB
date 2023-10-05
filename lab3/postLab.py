class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return f"You have successfully borrowed '{self.title}' by {self.author}."
        else:
            return f"'{self.title}' by {self.author} is already borrowed."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"You have returned '{self.title}' by {self.author}."
        else:
            return f"'{self.title}' by {self.author} is already available."

# Create some book instances
book1 = Book("Peer-e-Kamil", "Umera Ahmed")
book2 = Book("Maps for Lost Lovers", "Nadeem Aslam")
book3 = Book("Home Fire", " Kamila Shamsie")

# Borrow and return books
print(book1.borrow())  # Borrow 'Peer-e-Kamil'
print(book1.borrow())  # Already borrowed
print(book1.return_book())  # Return 'Peer-e-Kamil'
print(book2.borrow())  # Borrow 'To Kill a Mockingbird'
print(book3.borrow())  # Borrow 'Home Fire'
print(book1.return_book())  # Already available
