from discord.ext import commands
import discord
import json

error_color = 0xff0000
color = 0xededed

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Error Handler
    # If Person is the user who enters a command doesn't have the given perm
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      pre = prefixes[str(ctx.guild.id)] 

      if isinstance(error,commands.MissingPermissions):
        emb = discord.Embed(
          title="You can't do that",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)
        
      elif isinstance(error,commands.MissingRequiredArgument):
        emb = discord.Embed(
          title="Error",
          description=f'`{pre}help <command>`',
          colour=error_color)

        emb.set_footer(text=str(error))
        await ctx.reply(embed=emb)

      elif isinstance(error, commands.CommandNotFound):
        emb = discord.Embed(
          title="Command not Found",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

      elif isinstance(error, commands.MemberNotFound):
        emb = discord.Embed(
          title="Member not Found",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

      elif isinstance(error, commands.UserNotFound):
        emb = discord.Embed(
          title="User not Found",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

      elif isinstance(error,commands.CommandInvokeError):
        emb = discord.Embed(
          title="Error",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

        raise error

      elif isinstance(error,commands.MissingRole):
        emb = discord.Embed(
          title="You can't do that",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

      elif isinstance(error,commands.ChannelNotFound):
        emb = discord.Embed(
          title="Channel not Found",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

      elif isinstance(error,commands.RoleNotFound):
        emb = discord.Embed(
          title="Role not Found",
          description=str(error),
          colour=error_color)
        await ctx.reply(embed=emb)

      else:
        raise error

def setup(client):
    client.add_cog(ErrorHandler(client))