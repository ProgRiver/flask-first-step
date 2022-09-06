from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    # return """<ul>
    #             <li> First line </li>
    #             <li> Second string </li>
    #           </ul>"""
    
    # return """
    #         <h1>
    #             <ol>
    #                 <li> Первый пункт списка </li>
    #                 <li> Второй пункт списка </li>
    #             </ol>
    #         </h1>
    #        """

    return """
            <table align='center' border='2'>
                <tr>
                    <th> <u>Заголовок <br> № 1</u> </th>
                    <th> <u>Заголовок <br> № 2</u> </th>
                </tr>
                <tr>
                    <td> <b>Строка-1</b> <i>Колонка-1</i> </td>
                    <td> <b>Строка-1</b> <i>Колонка-2</i> </td>
                </tr>
                <tr>
                    <td> <b>Строка-2</b> <i>Колонка-1</i> </td>
                    <td> <b>Строка-2</b> <i>Колонка-2</i> </td>
                </tr>
            </table>
           """


if __name__ == "__main__":
    app.run(debug=True)