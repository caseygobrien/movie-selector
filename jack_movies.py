from datetime import datetime
from random import choice
from titlecase import titlecase
from smart_sort import smart_sort

running = True
movies = []
watched_movies = []
movielist = "jack movies.txt"
current_year = datetime.today().year
today = datetime.now().strftime('%m/%d')
this_years_list = "jack " + str(current_year) + " movies.txt"

open(movielist, 'a').close()
open(this_years_list, 'a').close()

with open(movielist, 'r') as movieimport:
    for line in movieimport:
        movies.append(line.strip('\n').lower())
with open(this_years_list, 'r') as watched:
    for line in watched:
        watched_movies.append(line.strip('\n'))


def save_movie_list():
    sorted_movies = smart_sort(movies)
    with open(movielist, 'r+') as save:
        for movie in sorted_movies:
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
    dated_title = today + ' ' + title
    watched_movies.append(dated_title)
    print('\n"{}" added to your {}'
          ' watched list.'.format(titlecase(title), current_year), end='\n')
    save_watched_list()


def add_new_movie(title):
    if title in movies:
        print("\n\"{}\" is already in your list".format(titlecase(title)), end='\n')
    else:
        movies.append(title)
        print('\n"{}" added to your list.'.format(titlecase(title)), end='\n')
        save_movie_list()


def delete_movie(title):
    if title in movies:
        movies.remove(title)
        save_movie_list()
        print("\n\"{}\" has been removed from your list".format(titlecase(title)), end='\n')
    else:
        print("\n\"{}\" is not in your list".format(titlecase(title)), end='\n')

while running:
    selection = input("""
[A]dd Movie
[D]elete Movie
[W]atch Movie
[R]andom Movie Selection
[S]ee Movie List
[V]iew Watched List
[E]xit
""").lower()
    if selection == "w":
        watched_movie = input("\nMovie Title: ")
        add_watched_movie(watched_movie)
    elif selection == "d":
        movie_to_delete = input("\nMovie Title: ")
        delete_movie(movie_to_delete)
    elif selection == "r":
        print("\nYour next movie should be \"{}\"".format(titlecase(choice(movies))))
    elif selection == "a":
        new_movie = input("\nMovie Title: ")
        add_new_movie(new_movie)
    elif selection == "s":
        view_sorted_movies = smart_sort(movies)
        print("-" * 40)
        for entry in view_sorted_movies:
            print(titlecase(entry))
        print("-" * 40)
    elif selection == "v":
        print("-" * 40)
        for entry in watched_movies:
            print(entry)
        print("-" * 40)
    elif selection == "e":
        running = False
