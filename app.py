from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>"Home page"</title>
            <meta charset="utf-8">
        </head>
        <body>
            <p>"Hello, my Flask"</p>
        </body>
    </html>
    <script>
        alert('Всплывающее окно...')
    </script>
    '''



if __name__ == "__main__":
    app.run()