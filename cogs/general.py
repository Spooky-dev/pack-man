from discord.ext import commands, tasks
import discord
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from itertools import cycle
import DiscordUtils

error_color = 0xff0000
color = 0xededed

# Statuses
updating_status = cycle(['updating'])
# status = cycle(['Ping to get prefix', 'nya ichi ni san', 'nya arigatou'])
status = cycle(['pm/help', 'https://github.com/spookyexe/pack-man'])

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cycle prefix upon bot activate
    @commands.Cog.listener()
    async def on_ready(self):
      self.change_status.start()

    # cycling status
    @tasks.loop(seconds=3)
    async def change_status(self):
      await self.client.change_presence(activity=discord.Game(next(status)))

    # A command that DMs the Bot Owner your suggestions
    @commands.command(aliases=["Suggest"])
    async def suggest(self, ctx, *, suggestion=None):

      bot_owner = self.client.get_user(695491063946674236)
      server = ctx.guild.name

      if suggestion == None:
        error_embed = discord.Embed(
          title='Error',
          description='Please enter a suggestion.',
          color=error_color
        )

        await ctx.send(embed=error_embed)

      else:
        # send suggestion to bot owner(spooky)
        owner_embed = discord.Embed(
          title='Suggestion',
          description=suggestion,
          timestamp=ctx.message.created_at,
          color=color
        )

        owner_embed.set_footer(
          text=f'**{server}**'
        )

        owner_embed.set_author(
        name=ctx.author.name,
        icon_url=ctx.author.avatar_url
        )

        await bot_owner.send(embed=owner_embed)

        # send to user that the suggestion was sent successfully
        user_embed = discord.Embed(
          title='Suggestion',
          description=f'{ctx.author.mention} thank you for suggesting!',
          color=color
        )

        await ctx.send(embed=user_embed)

    # To know how many server the bot is in
    @commands.command()
    @commands.is_owner() # only the bot owner can use this command
    async def servers(self, ctx):

      await ctx.send("I'm in `" + str(len(self.client.guilds)) + "` servers")
      await ctx.send('Servers connected to:')
      for guild in self.client.guilds:

        await ctx.send(guild.name)

    # Bot invite
    @commands.command()
    async def invite(self, ctx):
      await ctx.channel.send(
        # Embedded Buttons
          "Press Button to Invite Bot!",
          components=[
            Button(
              style=ButtonStyle.URL,
              label="Invite",
              url="https://github.com/Spooky-dev/pack-man"),
          ],
        )

    # Sends bot latency
    @commands.command(aliases=['Ping'])
    async def ping(self, ctx):
        # await ctx.reply(f'Pong! `{round(self.client.latency * 1000)}ms`')

        embed = discord.Embed(
          title='Pong 🏓',
          description=f'{round(self.client.latency * 1000)}ms',
          color=color
        )
        await ctx.send(embed=embed)

    # A command that DMs users from the bot owner
    @commands.command(aliases=["Tell"])
    @commands.is_owner() # only the bot owner can use this command
    async def tell(self, ctx, user: discord.User, *, message):
        
      await user.send(message)
      await ctx.reply(f"Sent {user.mention} the message!")

    # Bookmark Command, DMs the bookmarked message to the user
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, member:discord.Member):
      emoji = reaction.emoji

      if str(emoji) == '🔖':

        embed = discord.Embed(
          title='Bookmark',
          description=f'{reaction.message.content} - [**Jump To Message**]({reaction.message.jump_url})', 
          timestamp=reaction.message.created_at,
          color=color
        )

        embed.set_author(
            name=reaction.message.author,
            icon_url=reaction.message.author.avatar_url,
        )

        await member.send(embed=embed)


def setup(client):
    client.add_cog(General(client))