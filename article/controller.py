from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.articles_model = ArticleModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    #
    def check_user_answer(self, answer):
        if answer == "1":
            article = self.user_interface.add_user_article()
            self.articles_model.add_aticle(article)
        elif answer == "2":
            articles = self.articles_model.get_all_articles()
            self.user_interface.show_all_articles(articles)
        elif answer == '3':
            article_title = self.user_interface.get_user_article()
            try:
                article = self.articles_model.get_single_article(article_title)
            except KeyError:
                return self.user_interface.show_incorrect_title(article_title)
            else:
                self.user_interface.show_article(article)

        elif answer == '4':
            article_title = self.user_interface.get_user_article()
            try:
                article = self.articles_model.remove_article(article_title)
            except KeyError:
                return self.user_interface.show_incorrect_title(article_title)
            else:
                self.user_interface.del_article(article)

        elif answer == 'q':
            self.articles_model.save_data()
        else:
            self.user_interface.show_incorrect_answer(answer)

