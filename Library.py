from Book import Book,books

class Library:

    def __init__(self,name,city,books = []):
        self.name = name
        self.city = city
        #books is list of Book
        self.books = books

    def show_books(self):
        return self.books

    def add_book(self,book):
        if not isinstance(book,Book):
            print("Not valid book")
        else:
            self.books.append(book)
        

    
l = Library("Biblioteca publica","valencia")
for book in books:
    l.add_book(book)

print(*l.show_books())


