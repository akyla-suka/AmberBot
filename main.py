import os
import discord
from discord.ext import commands
from webserver import keep_alive

keep_alive()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'{bot.user} подключен к Discord!')


@bot.event
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles, id=1218528363845783603)
  await member.add_roles(role)


bot.run(TOKEN)
