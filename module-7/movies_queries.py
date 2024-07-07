import mysql.connector

config = {
    "user": "root",
    "password": "Bug2709$",
    "host": "localhost:3306",
    "database":" movies",
    "raise_on_warnings":True
    }

cursor = db.cursor()
cursor.execute ("SELECT studio_id, studio_name FROM studio")
studio = cursor.fetchall()
for studio in studio:
    print("studio_id: ()\n studio_name: ()n/".format (studio[1], studio[2], studio[3]))

cursor = db.cursor()
cursor.execute ("SELECT genre_id, genre_name FROM genre")
genre = cursor.fetchall()
for genre in genre:
    print ("genre_id: ()\n genre_name: ()\n" .format(genre[1], genre[2], genre[3]))
    
cursor = db.cursor()
cursor.execute ("SELECT film_name, film_runtime FROM film"
film = cursor.fetchall()
for film in film:
    print ("film_name: ()\n film_runtime: ()\n" .format(short film[1]), short film[2]))
    
cursor =db.cursor()
cursor.execute ('SELECT film_name, film_directors FROM film')
film = cursor.fetchall()
for film in film:
    print("film_name: ()\n film_director: ()\n" .format (director[1], director[2],director[3]))