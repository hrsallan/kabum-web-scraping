import sqlite3
import pandas as pd

banco = sqlite3.connect('productsDatabase.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (id integer, name text, " \
"quantity integer, numberOfRatings integer, scoreOfRatings integer " \
",price double, link text, imageUrl text, warranty text)")

#This reads the file we got from main.py, after web scrapping all the things we need
dataFrame = pd.read_excel(r"C:\kabum-web-scraping\data\hardware_products.xlsx")

#Go through all data in excel and add them into the sql
for index,row in dataFrame.iterrows():
    id = row["ID"]
    name = row["Name"]
    price = row["Price"]
    quantity = row["Quantity Available"]
    numberOfRatings = row["Number of Ratings"]
    scoreOfRatings = row["Score of Ratings"]
    link = row["URL"]
    imageUrl = row["Photos (g)"]
    warranty = row["Warranty"]
    values =(id, name, quantity, numberOfRatings, scoreOfRatings, price, link, imageUrl, warranty)
    idList = []
    count = 0
    print("Element " + str(index) + " has been read")
    for x in idList:
        if id == x:
            print("Found id :" + x)
            count = count + 1
    
    if count == 0:
        print("Inserting element : " + name)
        idList.append(id)
        cursor.execute("INSERT INTO products (id, name, quantity, numberOfRatings, scoreOfRatings, price, link, imageUrl, warranty) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
        banco.commit()
    else:
        print("Element: " + row["Name"] + " alredy satisfied!")
            
            
    #CREATE TABLE IF NOT EXISTS products (id integer, name text, " \
    #"quantity integer, numberOfRatings integer, scoreOfRatings integer " \
    #",price double, link text, imageUrl text, warranty text)
    #cursor.execute("INSERT INTO products VALUES ('"+id+"','"+name+"','"+quantity+"','"+numberOfRatings+"','"+scoreOfRatings+"','"+price+"','"+link+"','"+imageUrl+"','"+warranty+"')")

    

    
