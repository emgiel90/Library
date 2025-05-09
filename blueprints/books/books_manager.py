from tinydb import Query

def add_book_db(db,isbn,title,author):
     db.insert ({
         'isbn': isbn,
         'title': title,
         'author': author,
         'status': 'available'
        })

def get_all_books(db):
    return db.all()

def get_book(db, isbn):
    Book = Query()
    return db.search(Book.isbn == isbn)