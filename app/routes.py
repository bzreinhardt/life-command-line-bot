from flask import render_template, redirect, request, jsonify, abort, make_response
from app import app, db, bot
from app.models import User
#from firebase_admin import credentials, auth
import datetime
import traceback
import json
import pdb
import telegram
from app.mastermind import get_response, create_log


@app.route('/api/log', methods=['POST'])
def create_log_api():
    data = request.form.copy()
    print(data)
    print(data['type'])
    response = create_log(data)
    if response == 1:
        out = "Error creating log"
    else:
        out = response
    print(out)
    return jsonify({'status':out})


@app.route('/{}'.format(app.config['TOKEN']), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=app.config['URL'], HOOK=app.config['TOKEN']))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'


def get_user_from_token(token):
    user = None
    try:
        decoded_token = auth.verify_id_token(token)
        user = User.query.filter_by(social_id=decoded_token['user_id']).first()
    except Exception:
        # Session cookie is invalid, expired or revoked. Force user to login.
        traceback.print_exc()
    return user

def get_user_from_request(request):
    session_cookie = request.cookies.get('nameofyourapp')
    user = None
    if session_cookie:
        try:
            user = get_user_from_token(session_cookie)
        except auth.InvalidSessionCookieError:
            # Session cookie is invalid, expired or revoked. Force user to login.
            traceback.print_exc()
    if user:
        print(user.social_id)
    return user



@app.route('/sessionLogin', methods=['POST'])
def session_login():
    # Get the ID token sent by the client
    id_token = request.form['idToken']
    provider_data = json.loads(request.form['providerData'])

    # Set session expiration to 5 days.
    expires_in = datetime.timedelta(days=5)
    try:
        # Create the session cookie. This will also verify the ID token in the process.
        # The session cookie will have the same claims as the ID token.
        user = get_user_from_token(id_token)
        print(user)
        decoded_token = auth.verify_id_token(id_token)
        if not user:
            user = User(decoded_token['user_id'])
            db.session.add(user)
        if 'picture' in decoded_token:
            user.picture = decoded_token['picture']
        if 'email' in provider_data:
            user.email = provider_data['email']
        if 'name' in decoded_token:
            user.name = decoded_token['name']
        db.session.commit()
        response = jsonify({'status': 'success'})
        expires = datetime.datetime.now() + expires_in
        response.set_cookie('nameofyourapp', id_token, expires=expires)
        return response
    except Exception:
        traceback.print_exc()
        return abort(401, 'Failed to create a session cookie')


@app.route('/sessionLogout', methods=['GET','POST'])
def session_logout():
    response = make_response(redirect('/'))
    response.set_cookie('nameofyourapp', expires=0)
    return response



'''
@app.route('/')
@app.route('/index')
def index():
    user = get_user_from_request(request)
    render_login = True
    user_name = None
    if user:
        render_login = False
        user_name = user.name
    return render_template('index.html', user_name=user_name, render_login = json.dumps(render_login))
'''
