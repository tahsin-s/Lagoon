import discord
import logging
import fileio
import reminders
import time
from discord.ext import commands

#import token
with open('token.txt','r') as file:
    token = str(file.read())

# log setup
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#lgn commands
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='lgn ',intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def am(ctx):
    await ctx.send('yes')

@bot.command()
async def lbn(ctx):
    await ctx.send(fileio.getlink('Images',1))

@bot.command()
async def remind(ctx, member: discord.Member, *args):
    await ctx.send('remind called')
    await reminders.remind_set_time(ctx, member, args)

@remind.error
async def member_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find '+ctx.message.content.split()[2]+'... :|')

bot.run(token)