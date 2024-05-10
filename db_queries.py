import sqlite3
import os
autos = os.path.join(os.getcwd(),"db","Autos.db")
books = os.path.join(os.getcwd(),"db","Books.db")

db_paths = [autos,books]

for path in db_paths:
    con = sqlite3.connect(path)
    cur = con.cursor()

    if "Autos" in path:
        #distinct brands by splitting name using first element
        #origin fields??
        cur.execute("SELECT DISTINCT name FROM Autos;")
        names = cur.fetchall()
        brands = {}
        for name in names:
            brand = name[0].split()[0]
            if brand not in brands:
                brands[brand] = {"Amount":1,"Full Names":[name]}
            else:
                brands[brand]["Amount"] +=1
                brands[brand]["Full Names"].append(name)
        print("There are {} distinct brands".format(len(brands.keys())))
        for brand in brands:
            print("There are {} cars of brand {}".format(brands[brand]['Amount'],brand))
            for car in brands[brand]["Full Names"]:
                print(car)
                
                
        

    elif "Books" in path:
        #get distinct genres
        cur.execute("SELECT DISTINCT genre FROM Books;")
        genres = cur.fetchall()
        print("There are {} distinct genres".format(len(genres)))
        for genre in genres:
            print(genre)
        
        #publishers
        cur.execute("SELECT DISTINCT publisher FROM books;")
        publishers = cur.fetchall()
        print("There are {} distinct publishers".format(publishers))
        for publisher in publishers:
            print(publishers)

        #distinct authors
        cur.execute("SELECT DISTINCT author FROM Books;")
        authors = cur.fetchall()
        print("There are {} distinct authors".format(len(authors)))
        for author in authors:
            print(author)
    cur.close()
    con.close()
        

    
