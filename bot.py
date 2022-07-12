#this will handle all of the bot's communications with discord

import os
import discord
import methods

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
#gets the token from the .env file in the directory

bot = commands.Bot(command_prefix='!')
#sets the prefix for every command the bot responds to

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(guild.name)
        print(guild.id)
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='leaderboard', help='Provides the current top 100 NA leaderboard')
async def print_commands_list(ctx):
    if ctx.author == bot.user.name:
        #this makes sure it only responds to users and not bots, otherwise it might infinitely reply to itself
        return

    leaderboard = methods.print_leaderboard()
    quote_text = '```{}```'.format(leaderboard)
    await ctx.send(quote_text)


bot.run(TOKEN)

