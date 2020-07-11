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
       top_users.append({"name": user['name'], "abs_win": (user['win'] - user['loss']), "win": user['win'], "loss": user['loss']})

    top_users = sorted(top_users, key=lambda k: k['abs_win'], reverse=True)

    return top_users

fight = []
users = []

with open("users.json") as users_file:
    users = json.load(users_file)

# print(get_top_users())

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    user_name = request.form.get('user_name', '')
    user_pass = request.form.get('user_pass', '')
    btn_login = request.form.get('btn_login', 'LoginRefresh')
    btn_index = request.form.get('btn_index', '')
    btn_refresh = request.form.get('btn_refresh', '')
    result = request.form.get('result', '')
    the_kick = request.form.get('the_kick', '')
    the_block = request.form.get('the_block', '')
    my_result = request.form.get('my_result', '')
    enemy_result = request.form.get('enemy_result', '')
    kick = request.form.get('kick', '')
    block = request.form.get('block', '')

    if btn_refresh == 'refresh':
        i = 0
        for user in fight:
            if user['name'] == user_name and not user['enemy_result'] == '':
                result = user['result']
                my_result = user['my_result']
                enemy_result = user['enemy_result']
                del fight[i]
                break
            i += 1

        btn_login = 'fight'
        if not enemy_result == '':
            return render_template("game.html", user_pass=user_pass, user_name=user_name, the_kick=the_kick, the_block=the_block, my_result=my_result, enemy_result=enemy_result, result=result, kick=kick, block=block)

    if btn_index == 'index':
        for user in users:
            if user['name'] == user_name:
                user_win = user['win']
                user_loss = user['loss']
                break

        i = 0
        for user in fight:
            if user['name'] == user_name:
                del fight[i]
                break
            i += 1

        return render_template("index.html", user_pass=user_pass, user_name=user_name, top_users=get_top_users(), user_loss=user_loss, user_win=user_win)

    # if btn_refresh == 'refresh':
    #     return render_template("game.html", user_pass=user_pass, user_name=user_name, the_kick=the_kick, the_block=the_block)

    user1 = ''
    user2 = ''
    user3 = ''
    top_users = get_top_users()

    if len(top_users) > 0:
        user1 = top_users[0]['name'] + ': ' + str(top_users[0]['win']) + '/' + str(top_users[0]['loss'])
    if len(top_users) > 1:
        user2 = top_users[1]['name'] + ': ' + str(top_users[1]['win']) + '/' + str(top_users[1]['loss'])
    if len(top_users) > 2:
        user3 = top_users[2]['name'] + ': ' + str(top_users[2]['win']) + '/' + str(top_users[2]['loss'])

    if btn_login == 'Login':
        for user in users:
            if user['name'] == user_name:
                user_win = user['win']
                user_loss = user['loss']
                break
        if login(user_name, user_pass):
            return render_template("index.html", user_pass=user_pass, user_name=user_name, user_win=user_win, user_loss=user_loss)
        else:
            return render_template("login.html", user_pass="", user_name=user_name, error="Невірний пароль!")
    elif btn_login == 'LoginRefresh':
        return render_template("login.html", user_pass="", user_name=user_name, error="", user1=user1, user2=user2, user3=user3)
    elif btn_login == 'Quit':
        return render_template("login.html", user_pass="", user_name=user_name, error="", user1=user1, user2=user2, user3=user3)

    elif btn_login == 'fight':

        my_count = 0
        my_result = ""
        enemy_count = 0
        enemy_result = ""
        # result = ""

        if len(fight) > 0:
            enemy = fight[0]
            enemy_result1 = 'none'
            my_result1 = 'none'
            if not user_name == enemy['name']:
                if enemy['kick'] == block:
                    enemy_result = "Удар противника був зблокований"
                    enemy_result1 = "Противник зблокував ваший удар"
                else:
                    enemy_count = 1
                    enemy_result = "Ви пропустили удар противника"
                    enemy_result1 = "Ваший удар пройшов успішно"
                    my_result1 = "Ваший удар пройшов успішно"

                if kick == enemy['block']:
                    my_result = "Противник зблокував ваший удар"
                    enemy_result1 = "Удар противника був зблокований"
                    my_result1 = "Противник зблокував ваший удар"
                else:
                    my_count = 1
                    my_result = "Ваший удар пройшов успішно"
                    my_result1 = "Ви пропустили удар противника"

                if enemy_count == my_count:
                    result = "Нічия"
                    enemy['result'] = 'Нічія'
                elif enemy_count > my_count:
                    result = "Ви програли"
                    enemy['result'] = 'Ви перемогли'
                else:
                    result = "Ви перемогли"
                    enemy['result'] = 'Ви програли'

                enemy['enemy_result'] = enemy_result1
                enemy['my_result'] = my_result1

                for user in users:
                    if user['name'] == user_name:
                        if result == 'Ви перемогли':
                            user['win'] += 1
                        elif result == 'Ви програли':
                            user['loss'] += 1

                    if user['name'] == enemy['name']:
                        if result == 'Ви перемогли':
                            user['loss'] += 1
                        elif result == 'Ви програли':
                            user['win'] += 1

                with open("users.json", "w") as write_file:
                    json.dump(users, write_file)

                # del fight[0]
            else:
                result = "Очікування суперника"
        else:
            result = "Очікування суперника"
            not_user = True
            for user in fight:
                if user['name'] == user_name:
                    not_user = False

            if not_user == True:
                fight.append({"name": user_name, "kick": kick, "block": block, 'result': '', 'my_result': '', 'enemy_result': ''})

        if kick == '1':
            the_kick = "голову"
        elif kick == '2':
            the_kick = "корпус"
        else:
            the_kick = "ногу"

        if block == '1':
            the_block = "голови"
        elif block == '2':
            the_block = "корпуса"
        else:
            the_block = "ноги"

        return render_template("game.html", user_pass=user_pass, user_name=user_name, the_kick=the_kick, the_block=the_block, my_result=my_result, enemy_result=enemy_result, result=result, kick=kick, block=block)

if __name__ == "__main__":
    app.run()
