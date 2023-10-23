from view import UserInterface
from model import FilmModel


class Controller:
    def __init__(self):
        self.user_interface = UserInterface()
        self.film_model = FilmModel()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.get_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            film_dict = self.user_interface.add_film()
            self.film_model.add_new_film(film_dict)
        elif answer == '2':
            film_dict = self.film_model.show_all_films()
            self.user_interface.show_films(film_dict)
        elif answer == '3':
            film = self.user_interface.show_user_film()
            try:
                dict_film = self.film_model.show_film(film)
            except KeyError:
                self.user_interface.show_incorrect_film(film)
            else:
                self.user_interface.show_dict_film(dict_film)
        elif answer == '4':
            film = self.user_interface.show_user_film()
            try:
                self.film_model.remove_film(film)
            except KeyError:
                self.user_interface.show_incorrect_film(film)
            else:
                self.user_interface.del_user_film(film)
        elif answer == 'q':
            self.film_model.save_file()
        else:
            self.user_interface.show_incorrect_answer(answer)


