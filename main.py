# packages and modules
import discord
from discord.ext import commands
import os
import keep_alive
import json
from discord_components import DiscordComponents

# prefix
def get_prefix(client,message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

# Intents
intents = discord.Intents.default()
intents.members = True

# client
client = commands.Bot(
  command_prefix = get_prefix,
  help_command=None,
  intents=intents
  )

# on ready
@client.event
async def on_ready():
  print('Bot is Ready') # prints if the bot is online
  print(discord.__version__) # prints the discord.py version
  print('------')

  print('Servers connected to:' + str(len(client.guilds))) # number of servers the bot is conected to
  for guild in client.guilds: # gets all servers that the bot is connected to
    print(f'{guild.id} | {guild.name} | {guild.owner}') # prints the server id, name, and the server owner

  DiscordComponents(client) # discord components

# Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# runs and keep the bot alive
token = os.environ['TOKEN']
keep_alive.keep_alive()
client.run(token)