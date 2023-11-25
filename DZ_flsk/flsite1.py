from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "Информация", "url": "index"},
        {"name": "Каталог курсов", "url": "about"},
        {"name": "Добавить курс", "url": "contact"},
        ]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title='Информация', menu=menu)

@app.route("/about")
def about():
    return render_template("about.html", title='Каталог ресурсов', menu=menu)

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form)
    return render_template("contact.html", title='Добавить курс', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

if __name__ == '__main__':
    app.run(debug=True)