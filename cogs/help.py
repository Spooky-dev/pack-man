import discord
from discord.ext import commands
import DiscordUtils
import json

# Colors
error_color = 0xff0000
color = 0xededed

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, command=None):

        with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        note = f'Note: For more info about the command do `{pre}help <command>`. Do not include the `< >` upon typing the command and put quotation marks before and after each argument if argument is more than a word.\nExample: ```{pre}manifest resource "title title" "description description"```'

        if command is None:
            # Page 0
            embed_0 = discord.Embed(
                title='Help Command',
                description="Hello, I'm Pack-Man, a bot that can has lots of useful commands for pack making :)",
                color=color
            )
            embed_0.set_author(
                name='Spooky#0683',
                url='https://itsspooky.netlify.app/',
                icon_url='https://media.discordapp.net/attachments/836232703379505183/842762383616114708/spooky.png?width=630&height=630'
            )

            embed_0.set_thumbnail(
            url='https://media.discordapp.net/attachments/836232703379505183/842760616556625971/Pack-man.png?width=598&height=630')

            embed_0.set_footer(text=f'Note: React between ◀️ and ▶️ to move pages.\nRequested by {ctx.message.author.name}#{ctx.message.author.discriminator}')

            # Page 1
            embed_1 = discord.Embed(
                title='General Commands',
                description=note,
                color=color
            )

            embed_1.add_field(
                name='❥ Manifest Command',
                value=f' - Generates a `manifest.json`.\n```{pre}manifest <type> <pack_title> <pack_description>```',
                inline=False
            )

            embed_1.add_field(
                name='❥ UUID Command',
                value=f' - Generates a fresh version 4 UUID.\n```{pre}uuid```',
                inline=False
            )

            embed_1.add_field(
                name='❥ Color Codes Command',
                value=f' - A list of all Bedrock Color and Format Codes.\n```{pre}colorcodes```',
                inline=False
            )

            embed_1.add_field(
                name='❥ Texture Command',
                value=f' - Get any texture from the resource pack template, `<file_name>` is the file name of the block.\n```{pre}texture <type> <file_name>```',
                inline=False
            )

            # Page 2
            embed_2 = discord.Embed(
                title='Image Commands',
                description=note,
                color=color
            )

            embed_2.add_field(
                name='❥ Rotate Command',
                value=f' - Reply to any image then do command to rotate the image.\n```{pre}rotate <rotation_degrees>```',
                inline=False
            )

            embed_2.add_field(
                name='❥ Scale Command',
                value=f' - Reply to any small image then do command to scale image.\n```{pre}scale```',
                inline=False
            )

            embed_2.add_field(
                name='❥ Size Command',
                value=f' - Reply to any image then do command to get the size of the image.\n```{pre}size```',
                inline=False
            )
            
            # Page 3
            embed_3 = discord.Embed(
                title='Other Commands',
                description=note,
                color=color
            )
            embed_3.add_field(
                name='❥ Suggest Command',
                value=f' - Suggest anything to the bot.\n```{pre}suggest <suggestion>```',
                inline=False
            )

            embed_3.add_field(
                name='❥ Template Command',
                value=f' - All Resource and Behavior Pack Templates.\n```{pre}template```',
                inline=False
            )

            embed_3.add_field(
                name='❥ Invite Command',
                value=f' - Bot Invite Link.\n```{pre}invite```',
                inline=False
            )

            embed_3.add_field(
                name='❥ Ping Command',
                value=f' - Sends bot lantency.\n```{pre}ping```',
                inline=False
            )

            embed_3.add_field(
                name='❥ Change Prefix Command',
                value=f' - Change the bot prefix for this server.\n```{pre}changeprefix <new_prefix>```',
                inline=False
            )

            embed_3.add_field(
                name='❥ Bookmark Messages',
                value=f' - React to any new message with the emoji: ":bookmark:".\n``` ```',
                inline=False
            )
            

            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
            paginator.add_reaction('◀️', "back")
            paginator.add_reaction('▶️', "next")
            embeds = [embed_0, embed_1, embed_2, embed_3]

            await paginator.run(embeds)

        # Help Commands
        # if user enters manifest for <command>
        elif command.lower() == 'manifest':
            emb = discord.Embed(
            title='Manifest Command',
            description=f'`{pre}manifest <resource/behavior> <title> <description>`', 
            color=color
            )

            emb.add_field(
            name="Behavior", 
            value="for Behavior Packs", 
            inline=False
            )

            emb.add_field(
            name="Resource", 
            value="for Resource Packs", 
            inline=False
            )

            await ctx.send(embed=emb)

            emb = discord.Embed(
            title='Example:',
            description=f'```{pre}manifest resource "title title" "description description"```',
            color=color
            )

            emb.set_image(
            url='https://media.discordapp.net/attachments/836232703379505183/848832510926258176/unknown.png?width=617&height=512')

            await ctx.send(embed=emb)

        # if user enters changeprefix for <command>
        elif command.lower() == 'changeprefix':
            embed = discord.Embed(
            title='Change Prefix',
            description=f'```{pre}changprefix <new_prefix>```',
            color=color
            )

            await ctx.send(embed=embed)

        # if user enters scale for <command>
        elif command.lower() == 'scale':
            embed = discord.Embed(
            title='Scale',
            description=f'```{pre}scale```',
            color=color
            )

            await ctx.send(embed=embed)
            await ctx.send('https://imgur.com/Gn0afcH')

        # if user enters rotate for <command>
        elif command.lower() == 'rotate':
            embed = discord.Embed(
            title='Rotate',
            description=f'```{pre}rotate <rotation_degrees>```',
            color=color
            )

            await ctx.send(embed=embed)
            await ctx.send('https://imgur.com/f584Dqs')

        # if user enters uuid for <command>
        elif command.lower() == 'uuid':
            embed = discord.Embed(
            title='UUID',
            description=f'```{pre}uuid```',
            color=color
            )

            await ctx.send(embed=embed)

        # if user enters colorcodes for <command>
        elif command.lower() == 'colorcodes':
            embed = discord.Embed(
            title='Color Codes',
            description=f'```{pre}colorcodes```',
            color=color
            )

            await ctx.send(embed=embed)

        # if user enters template for <command>
        elif command.lower() == 'template':
            embed = discord.Embed(
            title='Template',
            description=f'```{pre}template```',
            color=color
            )

            await ctx.send(embed=embed)

        # if user enters invite for <command>
        elif command.lower() == 'invite':
            embed = discord.Embed(
            title='Invite',
            description=f'```{pre}invite```',
            color=color
            )

            await ctx.send(embed=embed)

        # if user enters ping for <command>
        elif command.lower() == 'ping':
            embed = discord.Embed(
            title='Ping',
            description=f'```{pre}ping```',
            color=color
            )

            await ctx.send(embed=embed)

        # if user enters suggest for <command>
        elif command.lower() == 'suggest':
            embed = discord.Embed(
            title='Suggest',
            description=f'```{pre}suggest <suggestion>```',
            color=color
            )

            await ctx.send(embed=embed)

        # of user enters get for <command>:
        elif command.lower() == 'texture':
            embed = discord.Embed(
            title='Get Texture',
            description=f'`{pre}texture <type> <file_name>`',
            color=color
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

            await ctx.send(embed=embed)
            await ctx.send('https://imgur.com/Snx4hI3')
            await ctx.send(f'renamed command from `{pre}get` to `{pre}texture`')

        elif command.lower() == 'size':
            embed = discord.Embed(
            title='Size',
            description=f'```{pre}size```',
            color=color
            )
            
            await ctx.send(embed=embed)
            await ctx.send('https://imgur.com/DOdRD1C')

        # Bookmark
        elif command.lower() == 'bookmark':
            embed = discord.Embed(
            title='Bookmark',
            description='React to any new message with "🔖", the bot will DM the message to you.',
            color=color
            )

            await ctx.send(embed=embed)
            await ctx.send('https://imgur.com/ULOkBlf')

          # help
        elif command.lower() == 'help':
          embed = discord.Embed(
            title='Help',
            description=f'```{pre}help [command]```',
            color=color
          )

          embed.set_footer(
            text='Note: arguments with `[ ]` are optional arguments.'
          )

          await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
            title='Error',
            description=f'Unkown Command: **{command}**',
            color=error_color
            )

            await ctx.send(embed=embed)
                


def setup(client):
    client.add_cog(General(client))