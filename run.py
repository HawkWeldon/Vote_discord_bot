########################################################################################
import discord 
from discord.ext import commands 
import os 
current_dirrectory = os.path.dirname(os.path.abspath(__file__))
########################################################################################
ind = discord.Intents.default()
ind.message_content = True
client = commands.Bot(command_prefix= "@@" , intents=ind)
########################################################################################
@client.event
async def on_ready():
    print("#"*150)
    print("Taking votes now")
    print("#"*150)
    user = client.user.name
# ready function to tell us the bot is working
########################################################################################
@client.command()
async def hello(text):
    await text.send("Hello there good sir")
########################################################################################
@client.command()
async def ping(text):
    await text.send("pong")
########################################################################################
@client.command()
async def pong(text):
        await text.send("ping")
########################################################################################
@client.command()
async def vote(text, *what):
    await text.send("Taking note")
    voting_path = "\Voting_list"
    path = current_dirrectory + voting_path
    await text.send(what)
    list = os.listdir(path)
    idx = 0
    while idx<len(list):
        if what[0] == list[idx]:
            path_write = path + '\\' + str(list[idx])
            path_num = path_write +'\\'+"num.txt"
            file = open(path_num, 'r+')
            L = file.readline()
            current_vote = int(L) + int(what[1])
            await text.send("Current votes = "+ str(current_vote))
            file.seek(0)
            file.write(str(current_vote))
            file.truncate()
            file.close
            path_log = path_write +'\\'+"log.txt"
            file = open(path_log, 'a+')
            L = str(text.author.name) + " : " + str(what[1])
            file.write("\n")
            file.write(L)
            file.close
            break
        idx = idx +1 
########################################################################################
@client.command()
async def help_more(text):
    await text.send("Mostlikely issues: \n 1> You used a capital letter where it should not be used or vise versa \n 2> For the list of things being voted on use ```@@list``` to check")
########################################################################################
@client.command()
async def list(text):
    voting_path = "\Voting_list"
    path = current_dirrectory + voting_path
    await text.send(os.listdir(path))
########################################################################################
file = open("Token.txt","r")
token = file.readline()
file.close()
client.run(token)