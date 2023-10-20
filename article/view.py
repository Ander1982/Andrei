def add_title(title):
    print(title)

    def wrap(fn):
        print(fn)

    return wrap


class UserInterface:
    @add_title('Ввод пользовательских данных'.center(50, "="))
    def wait_user_answer(self):
        # print("Ввод пользовательских данных".center(50, "="))
        print("Действия со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\nq- Выход из программы")
        user_answer = input("Выберете вариант действия: ")
        return user_answer

    def add_user_article(self):
        dict_articles = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        print(" Создание статьи ".center(50, "="))
        for key in dict_articles:
            dict_articles[key] = input(f'Введите {key} статьи:')
        print("=" * 50)
        return dict_articles

    def show_all_articles(self, articals):
        print(" Список статей: ".center(50, "="))
        for ind, article in enumerate(articals, 1):
            print(f"{ind}.{article}")
        print("=" * 50)
