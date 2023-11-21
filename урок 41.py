# SQLALchemy ORM

# import os
# from models1.database import DATABASE_NAME
# import create_database as db_creator
#
# if __name__ == "__main__":
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_creator.create_database()


# import os
#
# from models1.database import DATABASE_NAME
# import create_database1 as db_creator
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()

# шаблонизатор Jinja

from jinja2 import Template


# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a }} лет. Меня зовут {{ n }}.")
# msg = tm.render(n=name, a=age)
# print(msg)

# reg = {"name": "Игорь", "age": 28}
#
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.name }}.")
# msg = tm.render(p=reg)
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# reg = Person("Игорь", 28)
# print(reg.name)
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.name }}.")
# msg = tm.render(p=reg)
# print(msg)

# cities = [
#     {"id": 1, 'city': "Москва"},
#     {"id": 2, 'city': "Смоленск"},
#     {"id": 3, 'city': "Минск"},
#     {"id": 4, 'city': "Сочи"},
#     {"id": 5, 'city': "Ярославль"}
# ]
#
# link = """<select>
# {% for c in cities -%}
#     {% if c.id > 3 -%}
#          <option value='{{c["id"]}}'>{{ c['city'] }}</option>
#     {% elif c.city == "Москва" -%}
#          <option>{{ c['city'] }}</option>
#     {% else -%}
#          {{ c["city"] }}
#     {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# c = [
#     {"href": 'index', "n": "Главная"},
#     {"href": 'news', "n": "Новости"},
#     {"href": 'about', "n": "О компании"},
#     {"href": 'shop', "n": "Магазин"},
#     {"href": 'contact', "n": "Контакты"}
# ]
#
# l = """<ul>
# {% for k in c -%}
#     {% if k.n == "Главная" %}
#     <lu><a href="/{{k['href']}}" class="active">{{ k['n']}}</a></lu>
#     {% else -%}
#         <lu><a href="/{{k['href']}}">{{ k['n']}}</a></lu>
#     {% endif -%}
#     {% endfor -%}
# </ul>"""
# tm = Template(l)
# msg = tm.render(c=c)
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]

# tpl = "{{ cs | max(attribute='price') }}"
# tpl = "{{ (cs | max(attribute='price')).model }}"
# tpl = "{{ cs | sum(attribute='price') }}"
# tpl = "{{ cs | sort(attribute='model') }}"
# tpl = "{{ cs | random }}"

# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# макроопределения

# html = """
# {% macro input_text(name, value="", type="text", size=20) -%}
#     <input type="{{ type}}" name="{{ name }}" value="{{ value }}" size={{ size }}>
# {%- endmacro %}
#
# <p>{{ input_text("username")}}</p>
# <p>{{ input_text("email")}}</p>
# <p>{{ input_text("password")}}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# html = """
# {% macro input_text(type, name, placeholder) -%}
#     <input type="{{ type}}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro %}
#
# <p>{{ input_text("text", "firstname", "Имя")}}</p>
# <p>{{ input_text("text", "lastname", "Фамилия")}}</p>
# <p>{{ input_text("text", "address", "Адрес")}}</p>
# <p>{{ input_text("tel", "phone", "Телефон")}}</p>
# <p>{{ input_text("email", "email", "Почта")}}</p>
#
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# второй вариант

# html = """
# {% macro input_text(name, placeholder, type="text") -%}
#     <input type="{{ type}}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro %}
#
# <p>{{ input_text("firstname", "Имя")}}</p>
# <p>{{ input_text("lastname", "Фамилия")}}</p>
# <p>{{ input_text("text", "address", "Адрес")}}</p>
# <p>{{ input_text("phone", "Телефон","tel")}}</p>
# <p>{{ input_text("email", "Почта", "email")}}</p>
#
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# from  jinja2 import Environment, FileSystemLoader
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('shablon')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons, title="About Jinja", text="Содержимое сайта")
#
# print(msg)
#
# from jinja2 import Environment, FileSystemLoader
#
# subs = ["Культура", "Наука", "Политика", "Спорт"]
# file_loader = FileSystemLoader('shablon')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(list_table=subs)
#
# print(msg)

