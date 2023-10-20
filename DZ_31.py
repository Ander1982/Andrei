from bs4 import BeautifulSoup
import requests
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text

# def refinde(r):
#     return
def write_csv(data):
    with open("Sey7.csv", 'a', encoding="UTF-8") as f:
        write = csv.writer(f, delimiter=";", lineterminator='\r')
        write.writerow((data['Название салата'], data['ингредиенты'], data['ссылка']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("div", class_="lst")[0]
    l1 = p1.find_all("li", itemprop="itemListElement")
    for s in l1:
        dish = s.find('a').text
        # print(dish)
        ingredients = s.find("small").text
        # print(ingredients)
        url = s.find('a', itemprop="url")['href']
        # print(url)
        data = {'Название салата': dish, 'ингредиенты': ingredients, 'ссылка': url}
        # print(data)
        write_csv(data)


def main():
    url = "https://www.say7.info/cook/kitchen/38-Salatyi/"
    get_data(get_html(url))


if __name__ == "__main__":
    main()
