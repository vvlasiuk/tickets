from flask import Flask
from flask import render_template
import random
#from app import app

app = Flask(__name__)

a_count = 0
b_count = 0

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("index.html")

@app.route('/game/<choice>')
def game_choice(choice):
    global a_count
    global b_count
    a = choice
    c = ['камінь', 'ножиці', 'папір']
    b = random.choice(['1', '2', '3'])
    r = ""
    win = "Невідомий"
    if a == b:
        r = "нічия"
    elif (a == "1" and b == "2") or (a == "2" and b == "3") or (a == "3" and b == "1"):
        r = "Ви перемогли"
        a_count = a_count + 1
    else:
        r = "Ви програли."
        b_count = b_count + 1
    if a_count == 5:
        win = "Перемога за Вами. Ви перемогли бота з рахунком: " + str(a_count) + " : " + str(b_count)
        a_count = 0
        b_count = 0
    elif b_count == 5:
        win = "На жаль Ви програли. Бот переміг з рахунком: " + str(b_count) + " : " + str(a_count)
        a_count = 0
        b_count = 0
    return render_template("index.html",
                           a = c[int(a) - 1],
                           b = c[int(b) - 1],
                           r = r,
                           win = win,
                           a_count = a_count,
                           b_count = b_count)



if __name__ == "__main__":
    app.run()