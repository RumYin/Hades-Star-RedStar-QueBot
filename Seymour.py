import discord
import os
from discord.ext import commands

intents = discord.Intents.default() # Enable all intents except for members and presences
intents.members = True #allows members online to be seen
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready(): #will print back if bot is connected succesfully
    print('Bot is ready!')

@client.event
async def on_member_join(member): #message for member join, can be modfied
    print(f'(member)Has Joined a Server.')

@client.event
async def on_member_remove(member): # message for member exit, can be modified
    print(f'(member)Has Abandoned the Server')


client.run('***removed**')
