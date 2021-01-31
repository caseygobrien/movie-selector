import datetime
import random
from titlecase import titlecase

running = True
movies = []
watched_movies = []
movielist = "jack\'s movies.txt"
current_year = datetime.datetime.today().year
today = datetime.datetime.now().strftime('%m/%d')
this_years_list = "jack\'s " + str(current_year) + " movies.txt"

open(movielist, 'a').close()
open(this_years_list, 'a').close()

with open(movielist, 'r') as movieimport:
    for line in movieimport:
        movies.append(line.strip('\n').lower())
with open(this_years_list, 'r') as watched:
    for line in watched:
        watched_movies.append(line.strip('\n').lower())


def save_movie_list():
    with open(movielist, 'r+') as save:
        for movie in sorted(movies):
            save.write(titlecase(movie) + '\n')
            save.truncate()


def save_watched_list():
    with open(this_years_list, 'r+') as yearlist:
        for movie in watched_movies:
            yearlist.write(titlecase(movie) + '\n')
            yearlist.truncate()


def add_watched_movie(title):
    try:
        movies.remove(title)
        save_movie_list()
    except ValueError:
        pass
    title = today + ' ' + title
    watched_movies.append(title)
    print('\n"{}" added to your {}'
          ' watched list.'.format(titlecase(new_movie), current_year), end='\n')
    save_watched_list()


def random_movie():
    next_movie_number = random.randint(0, (len(movies)) - 1)
    next_movie = movies[next_movie_number]
    print("\nYour next movie should be \"{}\"".format(titlecase(next_movie)))


while running:
    new_movie = input("""\nEnter a movie title to add it to the list
Type \"watched\" to record a movie as watched
Press \"Enter\" to get a random movie selection
Type \"exit\" to quit\n""").lower()
    if new_movie == "exit":
        break
    elif new_movie == "":
        random_movie()
    elif new_movie in movies:
        print("\n\"{}\" is already in your list".format(titlecase(new_movie)), end='\n')
    elif new_movie == "watched":
        new_movie = input("\nEnter the title of the movie that you watched: ").lower()
        add_watched_movie(new_movie)
    elif new_movie.startswith("watched") is True:
        new_movie = new_movie.replace("watched ", "")
        add_watched_movie(new_movie)
    else:
        movies.append(new_movie)
        print('\n"{}" added to your list.'.format(titlecase(new_movie)), end='\n')
        save_movie_list()
