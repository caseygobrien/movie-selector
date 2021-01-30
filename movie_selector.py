from datetime import datetime
from random import choice
from titlecase import titlecase

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
    movies = sort_movies()
    with open(movielist, 'w') as save:
        for title in movies:
            print(titlecase(title), file=save)


def append_watched_movie(title):
    if title == '':
        return
    try:
        movies.remove(title)
        save_movie_list()
    except ValueError:
        pass
    new_title = today + ' ' + titlecase(title)
    watched_movies.append(new_title)
    with open(this_years_list, 'w') as save:
        for watched_movie in watched_movies:
            print(watched_movie, file=save)
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


def sort_movies():
    movies_with_the = [title for title in movies if title.startswith("the ")]
    movies_with_a = [title for title in movies if title.startswith("a ")]
    movies_with_an = [title for title in movies if title.startswith("an ")]
    movies_the_cleaned = [title.replace("the ", "") for title in movies_with_the]
    movies_a_cleaned = [title.replace("a ", "") for title in movies_with_a]
    movies_an_cleaned = [title.replace("an ", "") for title in movies_with_an]
    for title in movies:
        if title in movies_with_the:
            movies[movies.index(title)] = movies_the_cleaned[movies_with_the.index(title)]
        elif title in movies_with_a:
            movies[movies.index(title)] = movies_a_cleaned[movies_with_a.index(title)]
        elif title in movies_with_an:
            movies[movies.index(title)] = movies_an_cleaned[movies_with_an.index(title)]
    movies.sort()
    for title in movies:
        if title in movies_the_cleaned:
            movies[movies.index(title)] = movies_with_the[movies_the_cleaned.index(title)]
        elif title in movies_a_cleaned:
            movies[movies.index(title)] = movies_with_a[movies_a_cleaned.index(title)]
        elif title in movies_an_cleaned:
            movies[movies.index(title)] = movies_with_an[movies_an_cleaned.index(title)]
    return movies


while running:
    selection = input("""
[A]dd movie
[R]emove movie
[W]atch movie
[G]et Random movie
[S]ee movie list
[V]iew watched list
[X]it
""").lower()
    if selection == "a":
        add_movie(get_movie())
    elif selection == "r":
        remove_movie(get_movie())
    elif selection == "w":
        append_watched_movie(get_movie())
    elif selection == 's':
        movies = sort_movies()
        print('-' * 40)
        for entry in movies:
            print(titlecase(entry))
        print('-' * 40)
    elif selection == 'v':
        print('-' * 40)
        for entry in watched_movies:
            print(entry)
        print('-' * 40)
    elif selection == "g":
        print("\nYour next movie should be \"{}\"".format(titlecase(choice(movies))))
    elif selection == "x":
        print("You have {} movies in your list".format(len(movies)))
        running = False
