import requests
from bs4 import BeautifulSoup


class Info:
    html = ""
    r = []

    def __init__(self, url, file):
        self.url = url
        self.file = file

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

    def get_html(self):
        r = requests.get(self.url).text
        self.html = BeautifulSoup(r, "lxml")

    def parsing(self):
        l1 = self.html.find_all("li", itemprop="itemListElement")
        for s in l1:
            dish = s.find('a').text.strip()
            ingredients = s.find("small").text
            url = s.find('a', itemprop="url")['href']
            self.r.append({"dish": dish, "ingredients": ingredients, "url": url})

    def save(self):
        with open(self.file, 'w', encoding='utf-8-sig') as f:
            i = 1
            for item in self.r:
                f.write(
                    f"Номер салата №{i}\n\nНазвание: {item['dish']}\nСостав:{item['ingredients']}\nСсылка:{item['url']}\n{'*' * 30}\n")
                i += 1



