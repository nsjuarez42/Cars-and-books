class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __repr__(self):
        return "{},({},{})".format(type(self).__name__,self.title,self.author)

    def __str__(self):
        return "Title: {}, Author: {}".format(self.title,self.author)
    
    
        

books = [ Book("The Wealth of Nations","Adam smith"),
          Book("Surely You're Joking Mr Feynman","Richard Feynman")]
