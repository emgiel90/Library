from flask import Blueprint

Users = Blueprint('users', __name__, template_folder='templates')

@Users.route('/profile')
def profile():
    return 'Profile'