import sqlite3

#height is pages 
class Book:

    def __init__(self,title,author,genre,publisher):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pages = pages
        self.__publisher = publisher

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        if isinstance(title,str):
            self.__title = title
        else:
            raise ValueError

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self,author):
        if isinstance(author,str):
            self.__author = author
        else:
            raise ValueError
        
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self,genre):
        if isinstance(genre,str):
            self.__genre = genre
        else:
            raise ValueError

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self,pages):
        if isinstance(pages,str):
            self.__pages = pages
        else:
            raise ValueError

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self,publisher)
        if isinstance(publisher,str):
            self.__publisher = publisher
        else:
            raise ValueError

    def __repr__(self):
        return "{},({},{})".format(type(self).__name__,self.title,self.author)

    def __str__(self):
        return "Title: {}, Author: {}".format(self.title,self.author)
    
    
        

books = []
