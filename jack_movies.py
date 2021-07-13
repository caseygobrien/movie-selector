from datetime import datetime
from random import choice
from titlecase import titlecase

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
        watched_movies.append(line.strip('\n').lower())


def save_movie_list():
    sort_movies()
    with open(movielist, 'r+') as save:
        for movie in movies:
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
        elif title in movies_with_an:
            movies[movies.index(title)] = movies_an_cleaned[movies_with_an.index(title)]
        elif title in movies_with_a:
            movies[movies.index(title)] = movies_a_cleaned[movies_with_a.index(title)]
    movies.sort()
    for title in movies:
        if title in movies_the_cleaned:
            movies[movies.index(title)] = movies_with_the[movies_the_cleaned.index(title)]
        elif title in movies_an_cleaned:
            movies[movies.index(title)] = movies_with_an[movies_an_cleaned.index(title)]
        elif title in movies_a_cleaned:
            movies[movies.index(title)] = movies_with_a[movies_a_cleaned.index(title)]
    return movies


while running:
    selection = input("""\n[N]ew Movie
[W]atch Movie
[D]elete Movie
[R]andom Movie
[S]ee Movie List
[V]iew Watched List
[E]xit\n""").lower()
    if selection == "w":
        watched_movie = input("\nMovie Title: ")
        add_watched_movie(watched_movie)
    elif selection == "d":
        movie_to_delete = input("\nMovie Title: ")
        delete_movie(movie_to_delete)
    elif selection == "r":
        print("\nYour next movie should be \"{}\"".format(titlecase(choice(movies))))
    elif selection == "n":
        new_movie = input("\nMovie Title: ")
        add_new_movie(new_movie)
    elif selection == "s":
        view_sorted_movies = sort_movies()
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
