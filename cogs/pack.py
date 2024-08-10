# packages
from discord.ext import commands
import uuid
import discord
import json
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

note = '**NOTE:** UUIDs are already generated. There is no need to change them.'

error_color = 0xff0000
color = 0xededed

class Packs(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    # Sends Freshly Generated UUIDs
    @commands.command(aliases=['UUID', 'Uuid'])
    async def uuid(self, ctx):

      await ctx.send(
        # Embedded Buttons
          f"```{uuid.uuid4()}```",
          components=[
              [
                  Button(style=ButtonStyle.URL, label="uuid.generator.net", url="https://www.uuidgenerator.net/")
              ],
          ],
      )

    # Generates a Manifest File with UUIDs
    @commands.command(aliases=['Manifest'])
    async def manifest(self, ctx, type, title, description):

      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      pre = prefixes[str(ctx.guild.id)] 

      # For Resource Packs
      if type.lower() == 'resource':

        manifest = {
          "format_version": 2,
          "header": {
                "description": f"{description}",
                "name": f"{title}",
                "uuid": f"{uuid.uuid4()}",
                "version": [ 0, 0, 1 ],
                "min_engine_version": [ 1, 16, 0 ]
          },
          "modules": [
              {
                "type": "resources",
                "uuid": f"{uuid.uuid4()}",
                "version":  [ 0, 0, 1 ]
              }
          ]
      }

        await ctx.reply(f'```{json.dumps(manifest, indent=4, sort_keys=True)}```')
        await ctx.send(note)

      # For Behavior Packs
      elif type.lower() =='behavior':

        manifest = {
          "format_version": 2,
          "header": {
                "description": f"{description}",
                "name": f"{title}",
                "uuid": f"{uuid.uuid4()}",
                "version": [ 0, 0, 1 ],
                "min_engine_version": [ 1, 16, 0 ]
          },
          "modules": [
              {
                "type": "data",
                "uuid": f"{uuid.uuid4()}",
                "version":  [ 0, 0, 1 ]
              }
          ]
      }

        await ctx.reply(f'```{json.dumps(manifest, indent=4, sort_keys=True)}```')
        await ctx.send(note)

      # Error Handler
      else:
        embed = discord.Embed(
          title='Manifest Command',
          description=f'`{pre}manifest <resource/behavior> <title> <description>`', 
          color=error_color)

        embed.add_field(
          name="behavior", 
          value="for Behavior Packs", 
          inline=False)

        embed.add_field(
          name="resource", 
          value="for Resource Packs", 
          inline=False)

        embed.set_footer(
          text='Note: Do not invlude the `< >` upon typing the command and put `" "` before and after an argument for words that are more than one word')

        await ctx.reply(embed=embed)

        emb = discord.Embed(
          title='Example:',
          description=f'```{pre}manifest resource "title title" "description description"```',
          color=error_color
        )

        emb.set_image(
          url='https://media.discordapp.net/attachments/836232703379505183/848832510926258176/unknown.png?width=617&height=512')

        await ctx.send(embed=emb)

    # Sends Minecraft Color Codes etc
    @commands.command(aliases=['Colorcodes', 'ColorCodes'])
    async def colorcodes(self, ctx):

      embed=discord.Embed(
        title="Minecraft Color/Format Codes", 
        description="""
**Color Codes**
Black: §0
Dark Blue: §1
Dark Green: §2
Dark Aqua: §3
Dark Red: §4
Dark Purple: §5
Gold: §6
Gray: §7
Dark Gray: §8
Blue: §9
Green: §a
Aqua: §b
Red: §c
Light Purple: §d
Yellow: §e
White: §f

**Format Codes**
Reset: §r
Italic: §o
Bold: §l
Random Symbols: §k
New Line: (\ + n)""", 
        color=0xffffff)

      await ctx.reply(embed=embed)

    # Sends the resource/behavior pack template
    @commands.command()
    async def template(self, ctx):

      embed = discord.Embed(
        title='Minecraft Bedrock Template',
        description='Minecraft Bedrock Resource/Behavior Pack Templates',
        color=color
      )

      embed.add_field(
        name='Latest',
        value='https://www.minecraft.net/en-us/addons',
        inline=False
      )

      embed.add_field(
        name='All Versions/Betas',
        value='https://bedrock.dev/packs',
        inline=False
      )

      await ctx.reply(embed=embed)

      await ctx.send(
      # Embedded Buttons
      "Latest Direct Download: ",
      components=[
          [
              Button(style=ButtonStyle.URL, label="Resource", url="https://aka.ms/resourcepacktemplate"),
              Button(style=ButtonStyle.URL, label="Behavior", url="https://aka.ms/behaviorpacktemplate")
          ],
          ],
          )

def setup(client):
    client.add_cog(Packs(client))