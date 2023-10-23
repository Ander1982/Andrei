import pickle
import os.path


class Film:
    def __init__(self, name, genre, director, year, duration, studio, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.name}({self.genre})"


class FilmModel:
    def __init__(self):
        self.db_name = 'db_film.txt'
        self.list_film = self.load_file()

    def add_new_film(self, film_dict):
        films = Film(*film_dict.values())
        self.list_film[films.name] = films

    def show_all_films(self):
        return self.list_film.values()

    def show_film(self, film):
        film = self.list_film[film]
        dict_film = {
            "название фильма": film.name,
            "жанр": film.genre,
            "режиссер": film.director,
            "год выпуска": film.year,
            "длительность": film.duration,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, film):
        return self.list_film.pop(film)

    def save_file(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.list_film, f)

    def load_file(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()


