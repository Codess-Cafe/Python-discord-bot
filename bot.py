from discord.ext import commands
import random

from alive import keep_alive

import json
import requests


TOKEN = "#"


bot = commands.Bot(command_prefix='!')

@bot.command(name='faq', help='Searches the FAQ for the most relevant section corresponding to the provided keyword.')
async def faq(ctx, keyword):
    response = keyword
    await ctx.send(response)


@bot.command()
async def description(ctx):
    description = '''Hey there!!! I am **botname**. 
    I provide you a randome leetcode question everyday according to the difficulty level you need. 
    You can access my complete documentation here: https://github.com/Codess-Cafe/Python-discord-bot.
    I was made by some super talented mentess of Codess Cafe which provides pro-bono mentorship for collegiate women in tech.
    HAPPY LEARNING :)'''.
    await ctx.send(description)

def count (author) :
    '''
    A black box function that will depend on the implementation of the 
    post question feature to count number of problems solved by a user.
    '''
    solvedCount = 0
    return solvedCount

@bot.command (name = 'counter', help = 'Counts the number of questions solved by the user')
async def counter(ctx):
    response = f"{ctx.message.author.mention} you have solved {count(ctx.message.author)} problems"
    await ctx.send(response)



@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  mssg = ['hi', 'hello', 'hey']

  if message.content.lower().startswith(tuple(mssg)):
    greetings = ['Hey! How are you?', 'Hello! Glad to see you.']
    await message.channel.send(random.choice(greetings))


def get_qoute():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    msg = message.content
    if message.author == bot.user:
        return
    if 'quote' in msg.lower():
        response = get_qoute()
        await message.channel.send(response)
keep_alive()
bot.run(TOKEN)
