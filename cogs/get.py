import discord
from discord.ext import commands
import json

error_color = 0xff0000
color = 0xededed

with open("prefixes.json", "r") as f:
  prefixes = json.load(f)


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def texture(self, ctx, type, file_name):

      pre = prefixes[str(ctx.guild.id)] # prefix

      if type.lower() == 'item': # if user enters 'item' for 'type'
        try:
          await ctx.reply(file=discord.File(f'./cogs/items/{file_name}.png')) # get and send the texture with 'file_name.png'
        
        except: # item error
          embed = discord.Embed(
            title="Error",
            description=f'Invalid File Name: **{file_name}**',
            color=error_color
          )
          await ctx.reply(embed=embed)

      elif type.lower() == 'block': # if user enters 'block' for 'type'
        try:
          await ctx.reply(file=discord.File(f'./cogs/blocks/{file_name}.png')) # get and send the texture with 'file_name.png'
        
        except: # block error
          embed = discord.Embed(
            title="Error",
            description=f'Invalid File Name: **{file_name}.png**',
            color=error_color
          )
          await ctx.reply(embed=embed)

      else: # command error
        embed = discord.Embed(
          title='Error',
          description=f'`{pre}get <type> <file_name>`',
          color=error_color
        )

        embed.add_field(
          name='block',
          value='for block textures',
          inline=False
        )

        embed.add_field(
          name='item',
          value='for item textures',
          inline=False
        )

        await ctx.reply(embed=embed)
        await ctx.send('https://imgur.com/Snx4hI3')

    @commands.command() # for old command name
    async def get(self, ctx):

        pre = prefixes[str(ctx.guild.id)] 

        embed = discord.Embed(
          title='Error',
          description='Renamed command to `texture`',
          color=error_color
        )

        embed.add_field(
          name='Example:',
          value=f'```{pre}texture item diamond```'
        )

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Test(client))