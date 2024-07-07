import mysql.connector

config = {
    "user": "root",
    "password": "Bug2709$",
    "host": "localhost:3306",
    "database":" movies",
    "raise_on_warnings":True
    }

def show_films(cursor, title):

    cursor.execute("select film_name as Name, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

films = cursor.fetchall ()

print("\n  -- {} --".format(title))

for film in films:
    print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format (film[0], film[1], film[2], film[3]))