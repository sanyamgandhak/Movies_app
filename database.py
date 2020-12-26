#title ,relaese_datet ,watched


import datetime
import sqlite3

CREATE_MOVIES_TABLE='''CREATE TABLE IF NOT EXISTS MOVIES(
    TITLE TEXT,
    RELEASE_TIMESTAMP REAL,
    WATCHED INTEGER
)'''

INSERT_MOVIES="INSERT INTO MOVIES TITLE,RELEASE_TIMESTAMP VALUES(?,?);"

SELECT_ALL_MOVIES="SELECT * FROM MOVIES "

SELECT_UPCOMING_MOVIES="SELECT * FROM MOVIES WHERE RELEASE_TIMESTAMP > (?)"

SELECT_WATCHED_MOVIES="SELECT * FROM MOVIES WHERE WATCHED=1"

SET_MOVIE_WATCHED="UPDATE MOVIES SET WATCHED =1 WHERE TITLE=?;"
connection=sqlite3.connect('projdatabase1.db')

def create_tables():
     with connection:
         connection.execute(CREATE_MOVIES_TABLE)

def add_movie(TITLE0,RELEASE_TIMESTAMP):
    with connection:
        connection.execute("INSERT INTO MOVIES(TITLE,RELEASE_TIMESTAMP,WATCHED) VALUES (?,?,0)",(TITLE0,RELEASE_TIMESTAMP))

def get_movies(upcoming=False):
    with connection:
        cursor=connection.cursor()
        if upcoming:
            today_timestamp=datetime.datetime.today().timestamp()
            cursor.execute("SELECT * FROM MOVIES WHERE RELEASE_TIMESTAMP >(?)",(today_timestamp,))

        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movies(TITLE):
    with connection:
        connection.execute("UPDATE MOVIES SET WATCHED =1 WHERE TITLE = ?",(TITLE,))


def watched_movies():
    with connection:
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM MOVIES WHERE WATCHED =1")
        return cursor.fetchall()

