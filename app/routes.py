from flask import render_template, redirect, request, jsonify, abort, make_response
from app import app, db
from app.models import User
from firebase_admin import credentials, auth
import datetime
import traceback
import json

def get_user(request):
    session_cookie = request.cookies.get('session')
    user = None
    if session_cookie:
        try:
            decoded_token = auth.verify_id_token(session_cookie)
            user = {"name":decoded_token["name"]}
        except auth.InvalidSessionCookieError:
            # Session cookie is invalid, expired or revoked. Force user to login.
            traceback.print_exc()
    return user

@app.route('/sessionLogin', methods=['POST'])
def session_login():
    # Get the ID token sent by the client
    id_token = request.form['idToken']
    # Set session expiration to 5 days.
    expires_in = datetime.timedelta(days=5)
    try:
        # Create the session cookie. This will also verify the ID token in the process.
        # The session cookie will have the same claims as the ID token.
        session_cookie = auth.create_session_cookie(id_token, expires_in=expires_in)
        response = jsonify({'status': 'success'})
        expires = datetime.datetime.now() + expires_in
        response.set_cookie('session', id_token)
        return response
    except Exception:
        traceback.print_exc()
        return abort(401, 'Failed to create a session cookie')


@app.route('/sessionLogout', methods=['GET','POST'])
def session_logout():
    response = make_response(redirect('/'))
    response.set_cookie('session', expires=0)
    return response


@app.route('/')
@app.route('/index')
def index():
    user = get_user(request)
    render_login = True
    if user:
        render_login = False
    return render_template('index.html', user=user, render_login = json.dumps(render_login))
