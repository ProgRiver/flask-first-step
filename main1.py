from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1 align='center'><i>Information </i>О сайте</h1>"

    # target='_blank' - ссылка открывается в новой вкладке
    # return "<a href='https://github.com/ProgRiver' target='_blank'>My GitHub</a>"

    # return "<img src='https://python.org/static/img/python-logo.png' width='580' height='170'>"

    # return """<p align='center'>
    #             <img src='https://python.org/static/img/python-logo.png' width='580' height='170'>
    #           </p>"""

    # изображения в качестве ссылок
    return """<a href='https://python.org/' >
                <img src='https://python.org/static/img/python-logo.png' width='580' height='170'>
              </a>""" 


@app.route('/about')
def about():
    return "<h1>Следующая страница</h1>"


if __name__ == "__main__":
   app.run(debug=True)



# from operator import add, sub, mul, truediv, pow

# @app.route('/<float:a>/<op>/<float:b>/')
# def calc(a, op, b):
#     funcs = {'+': add, '-': sub, '*': mul, ':': truediv, '**': pow}
#     return render_template('index.html', a=a, funcs=funcs, op=op, b=b)

# template = '''
# {% if op not in funcs or (op == ":" and b == 0) %}
#     Ошибка
# {% else %}
#     {{ funcs[op](a, b) }}
# {% endif %}
# '''