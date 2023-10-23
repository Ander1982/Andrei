def add_title(title):
    def wramper(func):
        def wrap(*args, **kwargs):
            print(f'{title}'.center(50, "="))
            out_def = func(*args, **kwargs)
            print('*' * 50)
            return out_def

        return wrap

    return wramper


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def get_user_answer(self):
        print('Действия с фильмами: ')
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq -выход из программы")
        return input('Выберите вариант действия: ')

    @add_title('Введите данные нового фильма')
    def add_film(self):
        dict_film = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма")
        return dict_film

    @add_title('Список имеющихся фильмов')
    def show_films(self, film_dict):
        for ind, key in enumerate(film_dict, 1):
            print(f'Список фильмов: {ind}.{key}')

    @add_title('Название фильма')
    def show_user_film(self):
        return input("Введите интересуемый фильм")

    @add_title('Информация о фильме')
    def show_dict_film(self, dict_film):
        for key in dict_film:
            print(f"{key} - {dict_film[key]}")

    @add_title('Такого фильма нет в списке')
    def show_incorrect_film(self, film):
        print(f"Фильма с названием {film} в списке нет")

    @add_title('Фильм для удаления')
    def del_user_film(self, film):
        print(f'Фильм {film} удален')

    @add_title('Указанный запрос')
    def show_incorrect_answer(self, answer):
        print(f'Указанный Вами запрос {answer} отсутствует')