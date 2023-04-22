from flask import Flask, render_template, request, redirect, session
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

firebase_api_key = os.getenv("FIREBASE_API_KEY")
firebase_auth_domain = os.getenv("FIREBASE_AUTH_DOMAIN")
firebase_project_id = os.getenv("FIREBASE_PROJECT_ID")
firebase_storage_bucket = os.getenv("FIREBASE_STORAGE_BUCKET")
firebase_messaging_sender_id = os.getenv("FIREBASE_MESSAGING_SENDER_ID")
firebase_app_id = os.getenv("FIREBASE_APP_ID")
firebase_measurement_id = os.getenv("FIREBASE_MEASUREMENT_ID")
firebase_database_url = os.getenv("FIREBASE_DATABASE_URL")

config = {
    "apiKey": firebase_api_key,
    "authDomain": firebase_auth_domain,
    "projectId": firebase_project_id,
    "storageBucket": firebase_storage_bucket,
    "messagingSenderId": firebase_messaging_sender_id,
    "appId": firebase_app_id,
    "measurementId": firebase_measurement_id,
    "databaseURL": firebase_database_url
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    if ("user" in session):
        print(session['user'])
        return "Hi, {}".format(session['user']['email'])
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect('/')
        except:
            return "Invalid email or password"
    return render_template('home.html')


# criar conta
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if ("user" in session):
        print(session['user'])
        return "Hi, {}".format(session['user']['email'])
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            # session['user'] = user
            return redirect('/')
        except:
            return "Invalid email or password"
    return render_template('signup.html')


@app.route('/logout')
def logout():
    if ("user" not in session):
        return redirect('/')
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
