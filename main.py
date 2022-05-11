import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///makewish.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(30), nullable=False)
    SecondName = db.Column(db.String(30), nullable=False)
    Date = db.Column(db.DateTime, nullable=False)

    def __id__(self):
        return '<FirstName %r>' % self.id


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/SignIN")
def signin():
    return render_template('signin.html')


@app.route("/SignUp", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        FirstName = request.form.get('firstname')
        SecondName = request.form.get('secondname')
        Date = datetime.datetime.now()

        abc = request.form
        print(abc)

        user = User(FirstName=FirstName, SecondName=SecondName, Date=Date)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "При регистрации произошла ошибка:( Попробуйте позже!"
    else:
        return render_template('signup.html')


@app.route("/Catalog")
def catalog():
    return render_template('catalog.html')


@app.route("/Wish")
def wish():
    return render_template('wish.html')   


if __name__ == "__main__":
    app.run()