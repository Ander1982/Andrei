from flask import Flask, render_template, url_for, request, flash, session, redirect, g, abort
import sqlite3
import os
from DZ_flsk1.FDataBase import FDataBase

DATABASE = 'flsk1.db'
DEBUG = True
SECRET_KEY = 'f781103fd920dc1e30cbc3fc82fc05927813d9ea'
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'gfkb77t6r6cykio9uubtr6tr'
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsk1.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [{"name": "Информация", "url": "index"},
        {"name": "Каталог курсов", "url": "about"},
        {"name": "Добавить курс", "url": "contact"},
        ]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# @app.route("/index")
@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Информация", menu=dbase.get_menu(), course=dbase.get_course_anonce())


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['course']) > 10:
            res = dbase.add_course(request.form['name'], request.form['course'], request.form['url              '])
            if not res:
                flash('Ошибка добавления курса', category='error')
            else:
                flash('Курс внесен', category='success')

    return render_template("add_course.html", title='Добавление курсов', menu=dbase.get_menu())


@app.route('/course/<alias>')
def show_course(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, course = dbase.get_course(alias)
    if not title:
        abort(404)

    return render_template("course.html", menu=dbase.get_menu(), title=title, course=course)


@app.route("/about")
def about():
    return render_template("about.html", title='Каталог ресурсов', menu=menu)


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['course']) > 2:
            flash('Внесены корректные данные', category='success')
        else:
            flash('Ошибка ввода данных', category='error')

    return render_template("contact.html", title='Добавить курс', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Курс не найден', menu=menu)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
