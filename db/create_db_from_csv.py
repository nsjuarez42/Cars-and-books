import sqlite3
import os

dbs = {
    "Books":{
            "filename":"books.csv",
            "columns":{
                "Title":str,
                "Author":str,
                "Genre":str,
                "Height":int,
                "Publisher":str
                }
        },
    "Autos":{
            "filename":"Auto.csv",
            "columns":{
                "mpg":int,
                "cylinders":int,
                "displacement":int,
                "horsepower":int,
                "weight":int,
                "acceleration":float,
                "year":int,
                "origin":int,
                "name":str
                }
            
        }
    }

for name,db in dbs.items():
    filepath = os.path.join(os.getcwd(),db['filename'])

    #delete db if already exists
    if os.path.isfile(os.path.join(os.getcwd(),name+".db")):
        os.remove(os.path.join(os.getcwd(),name+".db"))

    con = sqlite3.connect(name+".db")
    cur = con.cursor()

    with open(filepath,encoding="utf-8") as file:
        lines = file.readlines()
        cols = lines[0].split(",")
        print("cols",cols)

        #CREATE TABLE
        create_data = []
        create_table = "CREATE TABLE {}(".format(name)
        for i,col in enumerate(cols):
            col_text= ""
            if  db['columns'][col.replace("\n","")]== str:
                col_text = "{} TEXT".format(col.replace("\n",""))
            elif db['columns'][col.replace("\n","")]== int:
                col_text = "{} INT".format(col.replace("\n",""))
            elif db['columns'][col.replace("\n","")] == float:
                col_text = "{} FLOAT".format(col.replace("\n",""))
            if i < len(cols) -1:
                print(col_text)
                col_text+=","   
            create_data.append(col_text)
        create_table += "".join(t for t in create_data) + ");"
        cur.execute(create_table)
                
        #INSERT DATA
        datas = []
        for line in lines[1:]:
            data = []
            line_data = []
            #split line by data
            if name is "Books":
                i=0
                splitted = [i.replace("\n","") for i in line.split(',')]
                while i < len(splitted):
                    if len(splitted[i]) >0 and splitted[i][0] == '"':
                        l = ""
                        l += splitted[i].replace('"','') + ","
                        i+=1
                        while len(splitted[i])>0 and splitted[i][-1] == '"' and i < len(splitted):
                            l+=splitted[i].replace('"','')
                            i+=1
                        line_data.append(l)
                    else:
                        line_data.append(splitted[i])
                        i+=1
            else:
                line_data = line.split(",")
            for i,d in enumerate(line_data):
                if i == len(line_data) - 1:
                    data.append(d.replace("\n",""))
                else:
                    data.append(d)
            datas.append(tuple(data))
            
        insert = "INSERT INTO {} VALUES(".format(name) +",".join(["?" for i in db['columns']])+ ");"
        cur.executemany(insert,tuple(datas))
        con.commit()
        cur.close()
        con.close()
##        cur.execute("SELECT * FROM {}".format(name))
##        for entry in cur.fetchall():
##            print(entry)
        #print(len(cur.fetchall()),"entries in ",name)
                
                
     
