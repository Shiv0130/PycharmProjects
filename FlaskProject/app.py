# from flask import Flask
#
# app = Flask(__name__)
#
# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Hello World</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             background-color: #f0f0f0;
#             margin: 0;
#             padding: 0;
#         }
#         .container {
#             margin-top: 20%;
#         }
#         h1 {
#             color: #333;
#             font-size: 3em;
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>Hello, World!</h1>
#     </div>
# </body>
# </html>
# """
#
# @app.route('/')
# def home():
#     return html_content
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, g, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)")
        db.commit()
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            cursor.execute("INSERT INTO messages (content) VALUES (?)", (message,))
            db.commit()
        return redirect('/')

    cursor.execute("SELECT content FROM messages ORDER BY id DESC LIMIT 1")
    message = cursor.fetchone()
    content = message[0] if message else "No messages found."

    print(message)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Message Recorder</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }}
            .container {{
                margin-top: 10%;
            }}
            h1 {{
                color: #333;
                font-size: 2em;
            }}
            input, button {{
                font-size: 1em;
                padding: 10px;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{content}</h1>
            <form method="POST">
                <input type="text" name="message" placeholder="Enter your message" required>
                <button type="submit">Save</button>
            </form>
        </div>
    </body>
    </html>
    """
    return html_content


if __name__ == '__main__':
    app.run(debug=True)

