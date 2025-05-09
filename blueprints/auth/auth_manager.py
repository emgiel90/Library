def signup(users_db, username, email, password):
     users_db.insert ({
         'username': username,
         'email': email,
         'password': password,
        })

def login(users_db,email,password):
     users_db.insert ({
         'email': email,
         'password': password,
        })
     
def forgot(users_db,email):
     users_db.insert ({
         'email': email
        })