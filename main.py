from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/SignIN")
def signin():
    return render_template('signin.html')

@app.route("/SignUp")
def signup():
    return render_template('signup.html')

@app.route("/Catalog")
def catalog():
    return render_template('catalog.html')

@app.route("/Wish")
def wish():
    return render_template('wish.html')   

if __name__ == "__main__":
    app.run()