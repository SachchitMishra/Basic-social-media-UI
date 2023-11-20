from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scroll")
def scroll():
    return render_template("scroll.html")

@app.route("/new_account")
def new_account():
    return render_template("new_account.html")

@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
