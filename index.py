from flask import Flask, Blueprint
from blueprints.auth import auth
from blueprints.books import books
from blueprints.users import users


app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'una_chiave_segreta_very_secret'

app.register_blueprint(auth.Auth)
app.register_blueprint(books.Book)
app.register_blueprint(users.Users)

@app.route('/')
def root():
    return "Benvenuti nella Biblioteca Personale!"

if __name__ == '__main__':
    app.run(debug=True) 
