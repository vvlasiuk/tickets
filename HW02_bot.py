import discord, random

a_count = 0
b_count = 0

TOKEN = 'NzIyMzUwOTI3MDEyNDI5ODI0.XuuYxA.WENpZMOttpy-1cJAgYkRg9o0udY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    c = ['камінь', 'ножиці', 'папір']
    b = random.choice(['1', '2', '3'])
    a = message.content

    global a_count
    global b_count

    if not (a == "!1" or a == "!2" or a == "!3" or a == "!0" or a == "!go"):
        msg = 'Очікується введення: !1, !2, !3, !0'.format(message)
        await message.channel.send(msg)
        return

    a = a.replace('!', '')

    if a == "go":
        msg = 'Гра камінь, ножиці, папір. \r\n!1 - камінь, !2 - ножиці, !3 - папір, !0 - закінчити гру'.format(message)
        await message.channel.send(msg)
        return

    if a == "0":
        msg = 'Ви покинули гру'.format(message)
        await message.channel.send(msg)
        a_count = 0
        b_count = 0
        return

    msg = 'Ваш хід: ' + c[int(a) - 1] + '\r\nХід бота: ' + c[int(b) - 1].format(message)
    await message.channel.send(msg)

    if a == b:
        msg = 'Нічия'.format(message)
        await message.channel.send(msg)
    elif (a == "1" and b == "2") or (a == "2" and b == "3") or (a == "3" and b == "!1"):
        msg = 'Ви перемогли'.format(message)
        await message.channel.send(msg)
        a_count = a_count + 1
    else:
        msg = 'Ви програли'.format(message)
        await message.channel.send(msg)
        b_count = b_count + 1

    msg = 'Ваш рахунок: ' + str(a_count) + '\r\nРахунок бота: ' + str(b_count).format(message)
    await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)