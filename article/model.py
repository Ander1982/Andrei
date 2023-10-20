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
        self.articles = {}

    def add_aticle(self, dict_article):
        article = Articale(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()
