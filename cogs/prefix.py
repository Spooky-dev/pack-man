from discord.ext import commands
import discord
import json

# get prefix
def get_prefix(client,message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

# colors
error_color = 0xff0000
color = 0xededed


class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    # on server join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):

      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      prefixes[str(guild.id)] = "pm/"

      with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

    # change prefix command
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def changeprefix(self, ctx, prefix):

      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix

      with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

      await ctx.send(f"The server prefix is now: **{prefix}**")

    # ping bot to get server prefix
    @commands.Cog.listener()
    async def on_message(self, message):

      if message.author == self.client.user:
        return
      if message.author.bot: return

      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      pre = prefixes[str(message.guild.id)] 

      if message.content.startswith('<@!842730997275557898'):
        embed = discord.Embed(
          title='Bot Server Prefix',
          description=f"Pack-Man's Prefix for this Server is : **{pre}**",
          color=color
        )
        await message.reply(embed=embed)

        # only works on pc ^^^
        
        await self.client.process_commands(message)

def setup(client):
    client.add_cog(Prefix(client))