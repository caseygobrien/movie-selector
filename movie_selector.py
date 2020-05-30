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


def save_movie_list():
    with open(movielist, 'w') as save:
        for movie in sorted(movies):
            print(titlecase(movie), file=save)


def append_watched_movie(title):
    if title == '':
        return
    try:
        movies.remove(title)
        save_movie_list()
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
        save_movie_list()
        print("\"{}\" removed from your list".format(titlecase(title)))
    else:
        print("\"{}\" is not in your list".format(titlecase(title)))


def add_movie(title):
    if title == '':
        return
    movies.append(title)
    print('\n"{}" added to your list.'.format(titlecase(title)), end='\n')
    save_movie_list()


def show_movie_list(list):
    print('-' * 40)
    for movie in sorted(list):
        print(titlecase(movie))
    print('-' * 40)


def get_movie():
    movie = input("Movie title: ").lower()
    return movie


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
        break
