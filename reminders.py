import datetime
import time
import discord
import schedule
import threading
from discord.ext import commands

#ask msg from user
async def waitmsg(ctx):
    client = discord.Client()
    userin = ''

    print('waiting')
    @client.event
    async def on_message(message):
        if message.author == ctx.author:
            userin = message.content
        return

    return userin
        
def printonce(ctx,msg):
    ctx.send(msg)
    return schedule.CancelJob
    
async def remind_set_time(ctx, member, note):

    await ctx.send('remind set time called')
    await ctx.send('When should I remind '+member.display_name+'? [dd/mm/yyyy hh:mm <am/pm>]')    
    msg = ' '.join(note)
    
    userin = await waitmsg(ctx)
    print(userin)
    
