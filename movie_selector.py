from datetime import datetime
from random import choice
from titlecase import titlecase

running = True
movies = []
movielist = "movies.txt"
current_year = datetime.today().year
this_years_list = str(current_year) + " movies.txt"
today = datetime.now().strftime('%m/%d')

open(movielist, 'a').close()

with open(movielist, 'r') as movieimport:
    for line in movieimport:
        movies.append(line.strip('\n').lower())


def save_movie_list(list_of_movies):
    sorted_movies = sort_movies(list_of_movies)
    with open(movielist, 'w') as save:
        for title in sorted_movies:
            print(titlecase(title), file=save)


def append_watched_movie(title):
    if title == '':
        return
    try:
        movies.remove(title)
        save_movie_list(movies)
    except ValueError:
        pass
    newtitle = today + ' ' + titlecase(title)
    with open(this_years_list, 'a') as save:
        save.write("\n" + newtitle)
    print('\n"{}" added to your {}'
          ' watched list.'.format(titlecase(title), current_year), end='\n')


def remove_movie(title):
    if title == '':
        return
    if title in movies:
        movies.remove(title)
        save_movie_list(movies)
        print("\"{}\" removed from your list".format(titlecase(title)))
    else:
        print("\"{}\" is not in your list".format(titlecase(title)))


def add_movie(title):
    if title == '':
        return
    if title in movies:
        print('\n"{}" is already in your list.'.format(titlecase(title)), end='\n')
        return
    movies.append(title)
    print('\n"{}" added to your list.'.format(titlecase(title)), end='\n')
    save_movie_list(movies)


def show_movie_list(list_of_movies):
    sorted_movies = sort_movies(list_of_movies)
    print('-' * 40)
    for movie in sorted_movies:
        print(titlecase(movie))
    print('-' * 40)


def get_movie():
    new_movie = input("Movie title: ").lower()
    return new_movie


def sort_movies(list_of_movies):
    sorted_movies = sorted(list_of_movies)
    movies_the_cleaned = []
    movies_a_cleaned = []
    movies_with_the = [title for title in sorted_movies if title.startswith("the ")]
    movies_with_a = [title for title in sorted_movies if title.startswith("a ")]
    for title in movies_with_the:
        movies_the_cleaned.append(title.replace("the ", ""))
        sorted_movies.remove(title)
    for title in movies_with_a:
        movies_a_cleaned.append(title.replace("a ", ""))
        sorted_movies.remove(title)
    for title in movies_the_cleaned:
        sorted_movies.append(title)
    for title in movies_a_cleaned:
        sorted_movies.append(title)
    sorted_movies.sort()
    for title in sorted_movies:
        if title in movies_the_cleaned:
            sorted_movies[sorted_movies.index(title)] = movies_with_the[movies_the_cleaned.index(title)]
        if title in movies_a_cleaned:
            sorted_movies[sorted_movies.index(title)] = movies_with_a[movies_a_cleaned.index(title)]
    return sorted_movies


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
        show_movie_list(movies)
    elif selection == 'v':
        watched_movies = []
        with open(this_years_list, 'r') as yearlist:
            for line in yearlist:
                watched_movies.append(line.strip('\n'))
        show_movie_list(watched_movies)
    elif selection == "g":
        print("\nYour next movie should be \"{}\"".format(titlecase(choice(movies))))
    elif selection == "x":
        print("You have {} movies in your list".format(len(movies)))
        running = False
