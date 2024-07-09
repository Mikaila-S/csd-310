import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost", user= "root", password= "Bug2709$", database= "movies"
)

print("--DISPLAYING studio RECORDS--")
mycursor = mydb.cursor()
mycursor.execute("SELECT studio_id, studio_name FROM studio")
studios = mycursor.fetchall()
for studio in studios:
    print("Studio ID:", studio[0])
    print("Studio Name", studio[1])



print("--DISPLAYING genre RECORDS--")
mycursor = mydb.cursor()
mycursor.execute("SELECT genre_id, genre_name FROM genre")
genres = mycursor.fetchall()
for genre in genres:
    print("Genre ID:", genre[0])
    print("Genre Name:", genre[1])

print("--DISPLAYING short film RECORDS--")
mycursor = mydb.cursor()
mycursor.execute("SELECT film_name, film_runtime FROM film")
films = mycursor.fetchall()
for film in films:
    print("Film Name:", film[0])
    print("Runtime:", film[1])

print("--DISPLAYING directors RECORDS--")
mycursor = mydb.cursor()
mycursor.execute("SELECT film_name, film_director FROM film")
films = mycursor.fetchall()
for film in films:
    print("Film Name:", film[0])
    print("Director", film[1])
