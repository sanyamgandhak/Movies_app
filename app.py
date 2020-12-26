import datetime
import database 

menu="""please select any option from below:
1)Add new movie
2)View upcoming movies 
3)View all movies
4)Marked Movie as Watched
5)view watched movie 
6)Exit

your choice :
"""

user_input=(input(menu))

database.create_tables()

def add_movie_fun():
    title=input('Movie Title: ')
    release_date=input('Release_date(dd-mm-yyy): ')
    parsed_date= datetime.datetime.strptime(release_date,"%d-%m-%Y")
    timestamp=parsed_date.timestamp()

    database.add_movie(title,timestamp)
    

def print_movie(heading,movies):
    print(f'--{heading} Movies--')
    for movie in movies:
        movie_date=datetime.datetime.fromtimestamp(movie[1])
        human_date=movie_date.strftime("%b %d %Y")
        #print(human_date)
        print(movie[0])
        print(human_date)
        print(movie[2])
        print('----\n')

def prompt_watch_movie():

    movie_title=(input("Please tell which movie you have watched: "))

    database.watch_movies((movie_title))



while(user_input!=6):
    if user_input=="1":
        add_movie_fun()
        user_input=(input(menu))
    elif user_input=="2":
        movies=database.get_movies(True)
        print_movie("Upcoming",movies)
        user_input=(input(menu))

    elif user_input=="3":
        movies=database.get_movies()
        print_movie("All",movies)
        user_input=(input(menu))

    elif user_input=="4":
        prompt_watch_movie()
        user_input=(input(menu))

    elif user_input=="5":
        movies1=database.watched_movies()
        print_movie("WATCHED ",movies1)
        user_input=(input(menu))
    else:
        print("invalid input\n")
        user_input(input(menu))
        

