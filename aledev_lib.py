import bcrypt
from datetime import datetime

salt = b'$2b$12$.SNNRQd0neb/k4DfuujBGu'

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(password, hashed):
    new_pass = hash_password(password)
    pass_hash = "b'" + hashed + "'"
    if str(new_pass) == str(pass_hash):
        return True
    else:
        return False

def Check_Birthday(birthday):
    try:
        fecha = datetime.strptime(birthday, "%d/%m/%Y")
        return True
    except ValueError:
        return False