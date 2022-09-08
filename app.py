from flask import Flask, render_template
from random import choice

app = Flask(__name__)

number = 150
# user_name = choice(("name-1", "name-2", "name-3", "name-4"))

@app.route("/")
def index():
    user_name = choice(("name-1", "name-2", "name-3", "name-4"))
    return render_template("index.html",
                           name=user_name,
                           project_number=number,
                           title="Home page")


if __name__ == "__main__":
    app.run(debug=True)