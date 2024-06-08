import re
import secrets


def verify_password(password):
    if re.match(r'^(?=.*[A-Z])(?=.*\W).{8,}$', password):
        return True
    else:
        return False

def generate_reset_token():
    return secrets.token_urlsafe(32)

USERNAME = 'travelhub@outlook.it'
PASSWORD = "" #deleted for privacy