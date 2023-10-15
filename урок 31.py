#  Парсинг сайтов
import re

from bs4 import BeautifulSoup

# f = open("index.html", encoding="utf-8").read()
# # print(f)
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find("div", id="whois")
# row = soup.find("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()

# print(row)

# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all('div', class_="row")
# copywriter = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
#
# print(copywriter)

# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

import requests

# r = requests.get('https://ru.wordpress.org/')


# print(r)
# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(r.text)

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     p1 = soup.find("header", id="masthead").find('p', class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_html(url))
#
#
# if __name__ == "__main__":
#     main()

# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         write = csv.writer(f, delimiter=";", lineterminator="\n")
#         write.writerow((data["name"], data["url"], data["rating"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find('h3').find('a').get('href')
#         # url = plugin.find('h3').find('a')['href']
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         date = {'name': name, "url": url, 'rating': r}
#         write_csv(date)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()


import requests
from bs4 import BeautifulSoup
import csv


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins_1.csv', 'a', encoding="utf-8-sig") as f:
#         write = csv.writer(f, delimiter=";", lineterminator="\n")
#         write.writerow((data["name"], data["url"], data["snippet"], data['active'], data['cy']))
#
#
# def get_date(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#
#         url = el.find("h3").find("a")["href"]
#         snippet = el.find("div", class_="entry-excerpt").text.strip()
#         active = el.find("span", class_="active-installs").text.strip()
#         c = el.find("span", class_="tested-with").text.strip()
#         cy = refind_cy(c)
#         date = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#
#         write_csv(date)
#
#
# def main():
#     for i in range(9, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_date(get_html(url))
#
#
# if __name__ == "__main__":
#     main()

from  parse_site import Parser

def main():
    pars = Parser("https://www.ixbt.com/live/index/news/", "new.txt")
    pars.run()


if __name__ == '__main__':
    main()