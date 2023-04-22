import pyrebase

config = {
    "apiKey": "AIzaSyBEuhhEmL_cYgrzn2yhou4mRIooo3hb904",
    "authDomain": "attendancelist-eb901.firebaseapp.com",
    "projectId": "attendancelist-eb901",
    "storageBucket": "attendancelist-eb901.appspot.com",
    "messagingSenderId": "470803604416",
    "appId": "1:470803604416:web:bc23f14ac919c1a0699e25",
    "measurementId": "G-JXGCHH0709",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = "teste@gmail.com"
password = "123456"

#user = auth.create_user_with_email_and_password(email, password)
#print(user)

user = auth.sign_in_with_email_and_password(email, password)

info = auth.get_account_info(user['idToken'])

print(info)