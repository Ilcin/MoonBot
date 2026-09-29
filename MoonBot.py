#!/usr/bin/env python
# -- coding: UTF-8 --
#print("Content-Type: text/plain;charset=utf-8")
#print("")
import discord, datetime, random, os, calendar, threading
from discord.ext import tasks
from discord.ext.commands import Bot
from moonbot_config import MOONBOT_CHARACTER, moontoken, ai_api_url, ai_api_key, valid_models, default_model

dirname, filename = os.path.split(os.path.abspath(__file__))
output = open(dirname+"/output.txt", "w")
output.write("Python code start")
intent = discord.Intents.all()
client = discord.Client(intents = intent)

bot = Bot(command_prefix='!', intents = intent)

# Message history for AI context (store last 5 messages per channel)
message_history = {}

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
l_think = ["think"]


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


async def call_ai_api(prompt: str, model: str = default_model) -> str:
    """Call the AI API directly and return the response"""
    print(f"[AI] Calling API with URL: {ai_api_url}")
    print(f"[AI] Using model: {model}")
    print(f"[AI] API Key configured: {'Yes' if ai_api_key else 'No'}")
    
    headers = {
        "Content-Type": "application/json",
    }
    if ai_api_key:
        headers["Authorization"] = f"Bearer {ai_api_key}"
        print(f"[AI] Authorization header set")
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": MOONBOT_CHARACTER[:100] + "..."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    
    try:
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(ai_api_url, json=payload, headers=headers) as response:
                print(f"[AI] Response status: {response.status}")
                print(f"[AI] Response headers: {response.headers}")
                
                if response.status == 200:
                    data = await response.json()
                    print(f"[AI] Success! Response: {data}")
                    return data.get("choices", [{}])[0].get("message", {}).get("content", "Thinking...")
                else:
                    error_text = await response.text()
                    print(f"[AI] Error response: {error_text}")
                    return f"AI API error: {response.status} - {error_text}"
    except Exception as e:
        print(f"[AI] Exception occurred: {str(e)}")
        return f"Error calling AI: {str(e)}"


async def handle_ai_response(message, remove_mention=False):
    """Handle AI response with message history context"""
    channel_id = message.channel.id
    context_messages = message_history.get(channel_id, [])
    
    # Build context from previous messages
    context_text = ""
    for msg in context_messages:
        context_text += f"{msg['author']}: {msg['content']}\n"
    
    # Add current message (optionally remove the mention)
    content = message.content
    if remove_mention:
        content = content.replace(f'<@!{client.user.id}>', '').replace(f'<@{client.user.id}>', '').strip()
    
    current_prompt = f"Previous conversation:\n{context_text}\n\nCurrent: {content}"
    
    await message.channel.send("I'm thinking about that...")
    response = await call_ai_api(current_prompt, default_model)
    await message.channel.send(response)
    
    # Update message history
    if channel_id not in message_history:
        message_history[channel_id] = []
    message_history[channel_id].append({
        'author': message.author.name,
        'content': message.content
    })
    # Keep only last 5 messages
    if len(message_history[channel_id]) > 5:
        message_history[channel_id] = message_history[channel_id][-5:]


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

    elif message.content.startswith('!clearhistory'):
        channel_id = message.channel.id
        if channel_id in message_history:
            del message_history[channel_id]
            await message.channel.send("Conversation history cleared for this channel.")
        else:
            await message.channel.send("No conversation history to clear.")

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
        await bot.login(moontoken, bot=True)

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
    
    elif check_for_words(l_think, message.content):
        await handle_ai_response(message)
    
    # Always respond when MoonBot is tagged
    elif client.user.mentioned_in(message):
        await handle_ai_response(message, remove_mention=True)
    
    # 10% chance to respond to any other message
    elif random.random() < 0.1:
        await handle_ai_response(message)


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
    days_in_year_str = str(days_in_year)
    dailymessage = str("Day " + day_of_year_str + " of " + days_in_year_str + ", " + remaining_days_str + " days remain")
    return dailymessage


output.write("Python code end")
client.run(moontoken)
bot.run(moontoken)

#client.close()
