def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f'{title}'.center(50, '='))
            output = func(*args, **kwargs)
            print('*' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных'.center(50, "="))
    def wait_user_answer(self):
        print("Действия со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\n3 - просмотр определенной статьи"
              "\n4 - удаление статьи"
              "\nq- Выход из программы")
        user_answer = input("Выберете вариант действия: ")
        return user_answer

    @add_title('Создание статьи: ')
    def add_user_article(self):
        dict_articles = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        for key in dict_articles:
            dict_articles[key] = input(f'Введите {key} статьи:')
        return dict_articles

    @add_title('Список статей: ')
    def show_all_articles(self, articals):
        for ind, article in enumerate(articals, 1):
            print(f"{ind}.{article}")

    @add_title('Поиск конкретной статьи: ')
    def get_user_article(self):
        article = input('Введите название статьи: ')
        return article

    @add_title('Сообщение об ошибке')
    def show_incorrect_title(self, article_title):
        print(f'В списке с названием {article_title} статьи нет')

    @add_title('Содержание статьи')
    def show_article(self, article):
        for key in article:
            print(f'В статье {key} {article[key]}')

    @add_title('Удаление статьи: ')
    def del_article(self, article):
        print(f'Статья {article} удалена')

    @add_title('Ошибка ввода')
    def show_incorrect_answer(self, answer):
        print(f'Запрос {answer} не существует')

