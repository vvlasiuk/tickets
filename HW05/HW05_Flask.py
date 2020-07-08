from flask import Flask
from flask import render_template
from flask import request
import json

def login(user_name, user_pass):
    global users

    if user_name == "":
        return False
    if user_pass == "":
        return False

    for user in users:
        if user['name'] == user_name:
            if user['pass'] == user_pass:
                return True
            else:
                return False

    users.append({"name": user_name, "pass": user_pass, "win": 0, "loss": 0})

    with open("users.json", "w") as write_file:
        json.dump(users, write_file)
    return True

def get_top_users():
    top_users = []
    for user in users:
       top_users.append({"name": user['name'], "win": (user['win'] - user['loss'])})



# a = open('users.json')
# b = a.read()
# print(b)

users = []


with open("users.json") as users_file:
    users = json.load(users_file)



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    user_name = request.form.get('user_name', '')
    user_pass = request.form.get('user_pass', '')
    btn_login = request.form.get('btn_login', 'Login')

    if btn_login == 'Login':
        if login(user_name, user_pass):
            return render_template("index.html", user_pass=user_pass, user_name=user_name)
        else:
            return render_template("login.html", user_pass="", user_name=user_name, error="Невірний пароль!")
    elif btn_login == 'Quit':
        return render_template("login.html", user_pass="", user_name=user_name, error="")

if __name__ == "__main__":
    app.run()
