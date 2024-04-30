import sqlite3

DATABASE = 'cars.db'

def print_all_carS():
    speed = input("What speed: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT car_name FROM car WHERE top_speed > ?;"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall()
        #print them nicely

        for car in results:
        print(f"car: {car[0]} Top speed : {car[1]}")

if __name__ == "__main__":
    print("Hello")
