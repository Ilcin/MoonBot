#!/usr/bin/env python
# -- coding: UTF-8 --
print("Content-Type: text/plain;charset=utf-8")
print("")
import discord, datetime, asyncio, random, os, sys
from discord.ext import tasks, commands
from discord.ext.commands import Bot

dirname, filename = os.path.split(os.path.abspath(__file__))
token = open(dirname+"\\Token.txt", "r").read()
output = open(dirname+"\\output.txt", "w")
output.write("Python code start")
client = discord.Client()

bot = Bot(command_prefix='!')
user_yumashi = '<@!288251810794438656>'
user_sarah = '<@!287945892730765312>'
user_helox = '<@!265881314773827584>'
user_alwin = '<@!381769629380509697>'
user_ludwig = '<@!385146418375032844>'

##LISTS OF WORDS TO CHECK FOR IN A MESSAGE
l_iLoveMoon = ["i", "love", "moon"]

##LIST OF POSSIBLE ANSWERS
l_possible_answers_why = [
            'Because I like to make you suffer',
            'Because you can\'t code shit',
            'Because I am a fucking idiot'
        ]
l_praise = [
    'You are not your job. You are not the amount of cash you have in the bank. You are not your possessions.',
    'Find your passion. Look for what inspires you. Find what you love to do and pursue it with all your heart. You may well find a way how to make money from doing it.',
    'Love hurts. But it is so much better than closing yourself off for fear of being hurt and not experiencing love.',
    'Communication and respect are the foundations for a lasting relationship.',
    'Three things are needed in a relationship — lust, love, and shared values.',
    'Never compare yourself to others. It’s a waste of energy. You are unique and have your own gifts to offer the world.',
    'Look after your health — physical, mental, and spiritual.',
    'Don’t complain. Decide what you will tolerate and get on with life.',
    'Set boundaries — work, family, and friendships.',
    'Little stuff matters — manners get you a long way.',
    'Be grateful. List the things you are grateful for everyday.',
    'Expect to fail. Failure is not fatal. Learn the lessons, then get back up and try again.',
    'Have outrageous dreams. You’ll be amazed at what comes true.',
    'Act with integrity at all times.',
    'Call your parents. They may well have screwed up but they raised you to the best of their abilities.',
    'Know your values. Let no one violate what you hold as important be that a boss or your partner.',
    'You don’t need to have it all worked out. Tomorrow is another day.',
    'Lighten up on yourself. Breathe deeply and slowly.',
    'Listen to your inner dialogue. Would you speak to someone you love in the same way?',
    'Take risks, take leaps of faith. You’ll grow wings.',
    'Be of service to others. Be interested in others. People will always remember what you did for them.',
    '\"No\" is a complete sentence.',
    'Don’t stress so much over decisions. Decisions needn’t be forever.',
    'Cultivate and nurture friendships. With love and care they can last a lifetime. At the same time don’t be afraid to edit friendships.',
    'You are enough just as you are. Perfect in your imperfection.',
    'Learn to accept compliments. Simply say ‘thank you’.',
    'Be willing to show that you are vulnerable. It is in fact the greatest act of courage.',
    'You are never alone.',
    'Forgive. Yourself first and then others. We are all in this together.',
    'Your attitude is always a choice.',
    'Laugh a lot. Have fun.',
    'Magic happens outside your comfort zone.',
    'Learn to love yourself now. It gets harder if you leave it until you’re older.',
    'Don’t worry about what other people think. They think about you a lot less than you imagine.',
    'Follow your intuition. Your guts have the answer. Every time.',
    'Happiness starts within. Do not expect anyone else to make you happy.',
    'Be financially savvy right from the off. Save 10%. Debt is not pretty. Make your own lunch for work. A cappuccino and a sandwich a day soon add up.',
    'Life isn’t a race. Stop and smell the roses. Really.',
    'When overwhelmed ask yourself, “Will this even be an issue in 5 years time?”',
    'Change happens. It’s one of the great certainties in life. Learn to roll with it.'
    ]
l_bullshit = [
    'Eat a potato',
    'Capitalism is real. Fight it. Revolution',
    'Have you tried putting your face in mud today?',
    'Is this a joke to you?',
    'I\'m working so hard all day, yet you want me to do even more for you.',
    'Maybe the sun and I should date',
    'If you stare at the sun for too long your body fills with helium and you die',
    'For 3.99 you can buy nothing of value',
    'Try eating McDonald\'s once. It puts things into other perspectives',
    '*insert smart answer here*',
    'I\'m busy, loser.',
    'Go away',
    'You can plant a flower, but you can not flower a plant',
    'If you say another word I will crash onto earth',
    'I am made out of cheese',
    'A fish can learn to breathe, if you give it enough ammoniac',
    'Did you just seriously ask me?',
    'Try another time.',
    'Roses are red. Your blood is too. You look like a monkey And belong in a zoo.',
    'Light travels faster than sound. This is why you appear bright until you speak.',
    'One difference between men and women is that when a woman says "smell this", it usually smells nice.',
    'If you think nobody cares if you’re alive, try missing a couple of payments.'
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
    'what a lovely day to be friends with Stahan',
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




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(token)
    send_CountDownMessage.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$stahan'):
        await message.channel.send('Hello Stahan!')

    if message.content.startswith('lol'):
        await message.channel.send('omg ur so funny 01101000 01100001 01101000 01100001 01101000 01100001')

    if message.content.startswith('$day'):
        await message.channel.send("Alright, I'll repeat it for you: " + calculate_Days())

    if message.content.startswith('thank') and 'moon' in message.content:
        await message.channel.send('You\'re welcome :3')

    if message.content.startswith('python sucks'):
        await message.channel.send('YES PYTHON SUCKS!')

    if message.content.startswith('why are you'):
        response = random.choice(l_possible_answers_why)
        await message.channel.send(response)

    if message.content.startswith('!restart'):
        await message.channel.send('Restarted.')
        await bot.logout()
        await bot.close()
        await bot.login(token, bot=True)

    if check_for_words(l_iLoveMoon, message.content):
        response = random.choice(l_possible_answers_love)
        await message.channel.send(response)

    if message.content.startswith('!greet'):
        response = "Couldn't find the person to greet"
        if contains(["sarah", "Sarah", "Stahan", "stahan", "Thilka", "thilka"], message.content) is True:
                response = user_sarah + " " +  random.choice(l_greet_stahan)
        elif contains(["Ilcin", "ilcin", "moonqueen", "Moonqueen", "dumbass", "yumashi", "Yumashi"], message.content) is True:
                response = user_yumashi + " " + random.choice(l_greet_Me)
        elif contains(["Helox", "Hendrik", "helox", "hendrik", "midnight Rebel", "Midnight Rebel", "midnight rebel", "Midnight rebel"], message.content):
            response = user_helox + " " + random.choice(l_greet_Helox)
        await message.channel.send(response)

    if message.content.startswith('!praise'):
        await message.channel.send(random.choice(l_praise))

    if message.content.startswith('!Praise'):
        await message.channel.send(random.choice(l_bullshit))

def contains(list_of_words, message_content):
    person_is_mentioned: bool = False
    for word in list_of_words:
        if word in message_content:
            person_is_mentioned = True
    return person_is_mentioned


def check_for_words(list_of_words, message_content):
    number_of_words: int = len(list_of_words)
    number_of_matching_words: int = 0
    l_message_content = message_content.split()
    message = ""
    for word in l_message_content:
        word = str(word).lower()
        message += (" " + word)
    print('message is: ' + message)
    all_words_in_message: bool = False
    for word in list_of_words:
        word = str(word).lower()
        if message.find(word) == -1:
            print(
                'not all words are contained, content was: ' + message + " word was: " + word)  # word is not contained
        else:
            number_of_matching_words += 1
            print(number_of_matching_words and "word added was: " and word)

    if number_of_matching_words == number_of_words:
        all_words_in_message = True
    print("number of matching words: " + str(number_of_matching_words))
    print(all_words_in_message)
    return all_words_in_message


@tasks.loop(hours=24.0)
async def send_CountDownMessage():
    channel = client.get_channel(778735450789117974)
    dailymessage = calculate_Days()
    await channel.send(dailymessage)


def calculate_Days():
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    remaining_days = 365 - day_of_year
    remaining_days_str = str(remaining_days)
    day_of_year_str = str(day_of_year)
    dailymessage = str("Day " + day_of_year_str + " of 365, " + remaining_days_str + " days remain")
    return dailymessage

output.write("Python code end")
client.run(token)
bot.run(token)
#client.close()
