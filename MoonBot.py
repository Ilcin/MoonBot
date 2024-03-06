#!/usr/bin/env python
# -- coding: UTF-8 --
#print("Content-Type: text/plain;charset=utf-8")
#print("")
import discord, datetime, random, os, calendar
from discord.ext import tasks
from discord.ext.commands import Bot

dirname, filename = os.path.split(os.path.abspath(__file__))
token = os.environ["moontoken"]
output = open(dirname+"/output.txt", "w")
output.write("Python code start")
intent = discord.Intents.default()
client = discord.Client(intents = intent)

bot = Bot(command_prefix='!', intents = intent)
user_yumashi = '<@!288251810794438656>'
user_sarah = '<@!287945892730765312>'
user_helox = '<@!265881314773827584>'
user_alwin = '<@!381769629380509697>'
user_ludwig = '<@!385146418375032844>'
user_chicken = '<@!699592578361983026>'

##LISTS OF WORDS TO CHECK FOR IN A MESSAGE
l_iLoveMoon = ["i", "love", "moon"]
l_randomQuestion = ["moon"]
l_lol = ["lol"]


##LIST OF POSSIBLE ANSWERS
dirname, filename = os.path.split(os.path.abspath(__file__))
file = open(dirname + '/OutputFiles/Praise.txt',"r",encoding='utf-8')
l_praise = file.read().splitlines()
file.close()
file = open(dirname + '/OutputFiles/Unpraise.txt',"r",encoding='utf-8')
l_unpraise = file.read().splitlines()
file.close()
file = open(dirname + '/OutputFiles/Puns.txt',"r",encoding='utf-8')
l_puns = file.read().splitlines()
file.close()
file = open(dirname + '/OutputFiles/ShutUpMoon.txt',"r",encoding='utf-8')
l_shutupmoon = file.read().splitlines()
file.close()
file = open(dirname + '/OutputFiles/GreetingsWithoutName.txt',"r",encoding='utf-8')
l_greetingsWithoutName = file.read().splitlines()
file.close()
file = open(dirname + '/OutputFiles/GreetingsWithName.txt',"r",encoding='utf-8')
l_greetingsWithName = file.read().splitlines()
file.close()
file = open(dirname + '/OutputFiles/RandomAnswers.txt',"r",encoding='utf-8')
l_randomAnswers = file.read().splitlines()
file.close()

l_possible_answers_why = [
            'Because I like to make you suffer',
            'Because you can\'t code shit',
            'Because I am a fucking idiot'
        ]

l_possible_answers_love = [
    'Thanks, I love you too! :3',
    'As you should, peasant',
    'That\'s right, kneel before me, fool',
    'Yeah? Prove it! Send me money',
    'How naive.'
]

l_greet_stahan = [
    'hello!!!!!!!!!!',
    'what a lovely day to be friends with Sarah',
    'Hello u wonderful',
    'looking good today!',
    'drink some water, stay healthy!'
]

l_greet_Helox = [
    'has left the chat (killed by <@!794949114466533376>)',
    'hello midnight rebel how are u',
    'I will end u',
    'what\'s up I\'m spamming you',
    'Eat a potato'
]

l_greet_Me = [
    'hello, ur ugly today!',
    'good morning u idiot',
    'hi I greet u'
]

l_greet_Chicken = [
    'idiot go away.',
    'good morning u idiot.',
    'stop looking at your phone and work!',
    'you are fired!',
    'stop being a bad influence on rustoff.',
    'you should see an eye doctor.',
    '... who is that? Never seen him before.',
    'are you made out of Nuggets?',
    'I really want to taste you fried.'
]

@client.event
async def on_ready():
    #('We have logged in as {0.user}'.format(client))
    #print(token)
    send_CountDownMessage.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!praise'):
        await message.channel.send(random.choice(l_praise))
    elif message.content.startswith('!Praise'):
        await message.channel.send(random.choice(l_unpraise))
    elif message.content.startswith('!pun'):
        await message.channel.send(random.choice(l_puns))
    elif message.content.startswith('shut up moon'):
        await message.channel.send(random.choice(l_shutupmoon))   
    elif message.content.startswith('!hello'):
        await message.channel.send(random.choice(l_greetingsWithoutName))

    elif message.content.startswith('$stahan'):
        await message.channel.send('Hello Stahan!')

    elif check_for_words(l_lol, message.content):
        await message.channel.send('omg ur so funny 01101000 01100001 01101000 01100001 01101000 01100001')

    elif message.content.startswith('$day'):
        await message.channel.send("Alright, I'll repeat it for you: " + calculate_Days())

    elif message.content.startswith('thank') and 'moon' in message.content:
        await message.channel.send('You\'re welcome :3')

    elif check_for_words(('python','sucks'),message.content):
        await message.channel.send('YES PYTHON SUCKS!')

    elif message.content.startswith('why are you'):
        response = random.choice(l_possible_answers_why)
        await message.channel.send(response)

    elif message.content.startswith('!restart'):
        await message.channel.send('Restarted.')
        await bot.logout()
        await bot.close()
        await bot.login(token, bot=True)

    elif check_for_words(l_iLoveMoon, message.content):
        response = random.choice(l_possible_answers_love)
        await message.channel.send(response)
    elif message.content.startswith('!greet'):
        msg = (message.content +'.')[:-1]
        await message.delete()
        response = "Hello there."
        if contains("@", msg):
            mentionedUser = msg.rsplit(' ',1)[1]
            if(mentionedUser == user_yumashi):
                #response = random.choice((mentionedUser + " " + random.choice(l_greet_Me), random.choice(l_greetingsWithName).replace('NAME',mentionedUser)))
                response = mentionedUser + " " + random.choice(l_greet_Me)
            elif(mentionedUser == user_helox):
                response = random.choice((mentionedUser + " " + random.choice(l_greet_Helox), random.choice(l_greetingsWithName).replace('NAME',mentionedUser)))
            elif(mentionedUser == user_sarah):
                response = random.choice((mentionedUser + " " + random.choice(l_greet_stahan), random.choice(l_greetingsWithName).replace('NAME',mentionedUser)))
            elif(mentionedUser == user_chicken):
                response = mentionedUser + " " + random.choice(l_greet_Chicken)
            else: response = random.choice(l_greetingsWithName).replace('NAME',mentionedUser)
        await message.channel.send(response)

    elif check_for_words(l_randomQuestion, message.content):
        await message.channel.send(random.choice(l_randomAnswers))
#    if message.content.startswith('!greet'):
#        response = "Couldn't find the person to greet"
#        if contains(["sarah", "Sarah", "Stahan", "stahan", "Thilka", "thilka"], message.content) is True:
#                response = user_sarah + " " +  random.choice(l_greet_stahan)
#        elif contains(["Ilcin", "ilcin", "moonqueen", "Moonqueen", "dumbass", "yumashi", "Yumashi"], message.content) is True:
#                response = user_yumashi + " " + random.choice(l_greet_Me)
#        elif contains(["Helox", "Hendrik", "helox", "hendrik", "midnight Rebel", "Midnight Rebel", "midnight rebel", "Midnight rebel"], message.content):
#            response = user_helox + " " + random.choice(l_greet_Helox)
#        await message.channel.send(response)



def contains(list_of_words, message_content):
    person_is_mentioned = False
    for word in list_of_words:
        if word in message_content:
            person_is_mentioned = True
    return person_is_mentioned


def check_for_words(list_of_words, message_content):
    number_of_words = len(list_of_words)
    number_of_matching_words = 0
    l_message_content = message_content.split()
    message = ""
    for word in l_message_content:
        word = str(word).lower()
        message += (" " + word)
    #print('message is: ' + message)
    all_words_in_message = False
    for word in list_of_words:
        word = str(word).lower()
        if message.find(word) == -1:
            return
            #print('not all words are contained, content was: ' + message + " word was: " + word)  # word is not contained
        else:
            number_of_matching_words += 1
            #print(number_of_matching_words and "word added was: " and word)

    if number_of_matching_words == number_of_words:
        all_words_in_message = True
    #print("number of matching words: " + str(number_of_matching_words))
    #print(all_words_in_message)
    return all_words_in_message


@tasks.loop(hours=24.0)
async def send_CountDownMessage():
    channel = client.get_channel(778735450789117974)
    dailymessage = calculate_Days()
    await channel.send(dailymessage)


def calculate_Days():
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    days_in_year = 365 + calendar.isleap(datetime.datetime.now().year)
    remaining_days = days_in_year - day_of_year
    remaining_days_str = str(remaining_days)
    day_of_year_str = str(day_of_year)
    dailymessage = str("Day " + day_of_year_str + " of " + days_in_year + ", " + remaining_days_str + " days remain")
    return dailymessage

output.write("Python code end")
client.run(token)
bot.run(token)

#client.close()
