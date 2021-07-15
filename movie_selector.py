from datetime import datetime
from random import choice
from titlecase import titlecase
from smart_sort import smart_sort

running = True
movies = []
watched_movies = []
movielist = "movies.txt"
current_year = datetime.today().year
this_years_list = str(current_year) + " movies.txt"
today = datetime.now().strftime('%m/%d')

open(movielist, 'a').close()
open(this_years_list, 'a').close()

with open(movielist, 'r') as movieimport:
    for line in movieimport:
        movies.append(line.strip('\n').lower())
with open(this_years_list, 'r') as watched_import:
    for line in watched_import:
        watched_movies.append(line.strip('\n'))


def save_movie_list():
    movies_sorted = smart_sort(movies)
    with open(movielist, 'w') as save_movies:
        for title in movies_sorted:
            print(titlecase(title), file=save_movies)


def append_watched_movie(title):
    if title == '':
        return
    try:
        movies.remove(title)
        save_movie_list()
    except ValueError:
        pass
    dated_title = today + ' ' + titlecase(title)
    watched_movies.append(dated_title)
    with open(this_years_list, 'w') as save_watched_list:
        for watched_movie in watched_movies:
            print(watched_movie, file=save_watched_list)
    print('\n"{}" added to your {}'
          ' watched list.'.format(titlecase(title), current_year), end='\n')


def remove_movie(title):
    if title == '':
        return
    try:
        movies.remove(title)
        save_movie_list()
        print("\"{}\" removed from your list".format(titlecase(title)))
    except ValueError:
        print("\"{}\" is not in your list".format(titlecase(title)))


def add_movie(title):
    if title == '':
        return
    if title in movies:
        print('\n"{}" is already in your list.'.format(titlecase(title)), end='\n')
        return
    movies.append(title)
    print('\n"{}" added to your list.'.format(titlecase(title)), end='\n')
    save_movie_list()


def get_movie():
    new_movie = input("Movie title: ").lower()
    return new_movie

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
    if selection == "a":
        add_movie(get_movie())
    elif selection == "d":
        remove_movie(get_movie())
    elif selection == "w":
        append_watched_movie(get_movie())
    elif selection == 's':
        view_sorted_movies = smart_sort(movies)
        print('-' * 40)
        for entry in view_sorted_movies:
            print(titlecase(entry))
        print('-' * 40)
    elif selection == 'v':
        print('-' * 40)
        for entry in watched_movies:
            print(entry)
        print('-' * 40)
    elif selection == "r":
        print("\nYour next movie should be \"{}\"".format(titlecase(choice(movies))))
    elif selection == "e":
        print("You have {} movies in your list".format(len(movies)))
        running = False
