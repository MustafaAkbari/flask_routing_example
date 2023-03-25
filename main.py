from flask import Flask

app = Flask(__name__)

# @app.route('/')
def hello_flask():
    return '<h1>Hello Flask</h1>'


# @app.rout('/about')
def about():
    return '<h1>This is about page</h1>'
app.add_url_rule('/','/', hello_flask)
app.add_url_rule('/about/', 'about/', about)





if __name__ == '__main__':
    app.run(debug=True)