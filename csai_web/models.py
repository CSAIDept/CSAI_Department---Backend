from csai_web import db
from sqlalchemy import event
import datetime
import jwt

#Authentication Part
class Login(db.Model):
    __tablename__ = 'UserDatabase'
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), primary_key=True)


def encode_auth_token(email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
            'iat': datetime.datetime.utcnow(),
            'email': email
        }
        return jwt.encode(
            payload,
            'b7b10848586a9043fe7520b9d57e00cb',
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, 'b7b10848586a9043fe7520b9d57e00cb')
        return payload['email']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'