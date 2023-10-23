import pickle
import os.path
class Articale:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __str__(self):
        return f"{self.title}({self.author})"


class ArticleModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.articles = self.load_file()

    def add_aticle(self, dict_article):
        article = Articale(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, article_title):
        article = self.articles[article_title]
        dict_articles = {
            "название": article.title,
            "автор": article.author,
            "количество страниц": article.pages,
            "описание": article.description
        }
        return dict_articles

    def remove_article(self, article):
        return self.articles.pop(article)

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)

    def load_file(self):
        if os.path.exists(self.db_name):
             with open(self.db_name, 'rb') as f:
                  return pickle.load(f)
        else:
            return dict()



