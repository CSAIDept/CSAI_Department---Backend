import json
from flask import request, jsonify, g, make_response
from csai_web.models import Login, db, encode_auth_token
from csai_web import app
from csai_web.middleware import login_required

@app.route('/csaiweb/backend/auth', methods=["POST"])
def login():
    content = request.get_json()
    username = content["username"]
    email = content["email"]

    user = Login.query.filter(Login.email == email).first()

    if user is None:
        user_in = Login(username=username, email=email)
        db.session.add(user_in)
        db.session.commit()

    token = encode_auth_token(email)

    dict = {
        'token': token.decode()
    }

    return make_response(jsonify(dict))


@app.route('/csaiweb/backend/auth', methods=["GET"])
@login_required
def decode_email():
    try:
        email = g.user

        res = Login.query.filter(Login.email == email).first()

        List = []
        
        dict = {
            'username': res.username,
            'email': res.email
        }
        List.append(dict)

        return json.dumps(List)
    except:
        return 'server error', 500   