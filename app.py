#docstring - Tamim Alawi - LV shoe database 
#import 
import sqlite3

#constant and variable
DATABASE = "assment.db"

#function    
def print_all_shoes():
    '''print all shoe nicely'''
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT * FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print(f"{'Name':<25}{'price':<10}{'size':<9}{'materials':<30}{'description':<15}")
    for shoe in results: 
       print (f"{shoe[1]:<25}{shoe[2]:<10}{shoe[3]:<9}{shoe[4]:<30}{shoe[5]:<15}") 
    db.close()


def shoename_price():
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT shoe_name,price FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print(f'name                          price')
    for shoe in results:
        print(f"{shoe[0]:<30}{shoe[1]:<5}")
    db.close()
    

def description():
    '''print description size nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT shoe_name, size, description FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print(f'name                    size      description')
    for shoe in results:
        print(f"{shoe[0]:<25}{shoe[1]:<13}{shoe[2]:<15}") 
    db.close()    


def material():
    '''print material'''
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT shoe_name, material FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                     material")
    for shoe in results:
        print(f"{shoe[0]:<25}{shoe[1]:<100}")
    db.close()  


def shoename_price_expensive_cheapest():
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT shoe_name,price FROM shoe ORDER BY price DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          price")
    for shoe in results:
        print(f"{shoe[0]:<30}{shoe[1]:<10}")
    db.close()      

def shoename_description():
    '''print description'''
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT shoe_name, description FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          description")
    for shoe in results:
        print(f"{shoe[0]:<30}{shoe[1]:<25}")
    db.close()      

def shoename_price_size():
    '''print price size'''
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT shoe_name,price,size,material FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                             price              size   ")
    for shoe in results:
        print(f"{shoe[0]:<33}{shoe[1]:<20}{shoe[2]:<15}")
    db.close()      

def shoename_material_description():
    db = sqlite3.connect("shoes.db")
    cursor = db.cursor()
    sql = "SELECT shoe_name,description,material FROM shoe;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                          description                                                                                                                        material")
    for shoe in results:
        print(f"{shoe[0]:<30}{shoe[1]:<131}{shoe[2]:<50}")
    db.close()


#main loop

    
while True:
    user_input = input(
"""
What would you like to do.
n1. print all shoe
n2. print shoename and price 
n3. print description and size
n4. print material
n5. print shoename and price from most expensive to cheapest
n6. print shoename and description
n7. print shoename and price and size
n8. print shoename and material and description
n9.Exit

""")
    if user_input == "1":
        print_all_shoes()
    elif user_input == "2":
        shoename_price()
    elif user_input == "3":
        shoename_description()
    elif user_input == "4":
        material()
    elif user_input == "5":
        shoename_price_expensive_cheapest()
    elif user_input == "6":
        shoename_description()
    elif user_input == "7":
        shoename_price_size()
    elif user_input == "8":
        shoename_material_description()
    elif user_input == "9":
        break
    else:

        print("That was not an option brav but\n")
        print("Do you want a can off fanta lime brav?\n")
    #ask user for option

    #if they type "1"- print all shoes
