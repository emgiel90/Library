from flask import Blueprint, render_template, request, redirect, url_for
from tinydb import TinyDB
from tinydb import Query
from blueprints.books.forms import AddBookForm, SearchBookForm
from blueprints.books.books_manager import add_book_db, get_all_books, get_book
from blueprints.auth.auth_manager import signup, login, forgot
from blueprints.auth.forms import RegistrationForm,LoginForm, ForgotPasswordForm

Book = Blueprint('books', __name__, template_folder='templates', url_prefix='/book')

db = TinyDB('./database/db.json')
users_db = TinyDB('./database/users_db.json')

@Book.route('/')
def root():
    return render_template("layout.html")


@Book.route('/home', methods=['GET','POST'])
def home():
    books = get_all_books(db)
    print(books)
    return render_template("home.html", books=books)

@Book.route('/removeBook/<isbn>', methods=['GET','POST','DELETE'])
def removeBook(isbn): 
    Book = Query()
    db.remove(Book.isbn == isbn)
    return redirect(url_for('books.home'))


@Book.route('/book/<isbn>', methods=['GET','POST'])
def book(isbn):
    books = get_book(db, isbn)
    return render_template("book.html", books=books)


@Book.route("/add", methods=['GET','POST']) 
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        add_book_db(db, form.isbn.data, form.title.data, form.author.data)
        return redirect(url_for('books.home'))
    return render_template("add_book.html", form=form)

@Book.route("/searchB", methods=['GET','POST']) 
def searchB():
    form = SearchBookForm()
    if form.validate_on_submit():
        Book = Query()
        if db.contains(Book.title == form.title.data.capitalize()):
            return render_template('found.html')
        else:
            return render_template('unfound.html')
    return render_template("searchB.html", form=form)



@Book.route('/register', methods=['GET','POST'])
def signUp() -> str:
    form: RegistrationForm = RegistrationForm()
    if form.validate_on_submit():
        signup(users_db, form.username.data, form.email.data, form.password.data)
        return render_template('success.html')
    return render_template('register.html', form=form)

@Book.route('/login', methods=['GET', 'POST'])
def log():
    form = LoginForm()
    if form.validate_on_submit():
        login(users_db, form.email.data, form.password.data)
        return redirect(url_for('books.home'))
    return render_template('login.html', form=form)

@Book.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit(): 
        forgot(users_db, form.email.data)
        return render_template('password.html')
    return render_template('forgot-password.html', title='Recupera la tua password', form=form)
