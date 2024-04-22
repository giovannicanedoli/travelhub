import re
import secrets


def verify_password(password):
    if re.match(r'^(?=.*[A-Z])(?=.*\W).{8,}$', password):
        return True
    else:
        return False

def generate_reset_token():
    return secrets.token_urlsafe(32)  # Genera un token di 32 caratteri

USERNAME = 'travelhub@outlook.it'
PASSWORD = "pPT9}Qsx*Ae%C)<j7]Y'yH"
