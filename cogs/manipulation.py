from discord.ext import commands
import discord
from PIL import Image
from io import BytesIO
import asyncio
import aiohttp
import json

# colors
error_color = 0xff0000
color = 0xededed

# get server bot prefix
with open("prefixes.json", "r") as f:
  prefixes = json.load(f)

# extensions
pic_ext = ['.jpg','.png','.jpeg'] # Extensions

class Manipulation(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.ses = aiohttp.ClientSession()

    # no image error
    async def no_image(self, ctx):
      embed = discord.Embed(
          title='Error',
          description='There are no images in that message.',
          color=error_color
        )
      await ctx.send(embed=embed)

    # no replied message error
    async def no_reply(self, ctx):
      embed = discord.Embed(
          title='Error',
          description='Reply to an image with that command to execute command.',
          color=error_color
        )
      await ctx.send(embed=embed)

    # scale command
    @commands.command()
    async def scale(self, ctx):
      try:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id) # get replied message

        
        if len(message.attachments) > 0: # Checks if there are attachments to messages
          for file in message.attachments:
            for pic in pic_ext:
              
              if file.filename.endswith(pic):

                attachment = message.attachments[0]

                url = attachment.url # Get attachment url

                async with self.client.ses.get(url) as r:
                  if r.status in range(200, 299):
                    
                    img = Image.open(BytesIO(await r.read()), mode='r') # Open Image URL
                    width, height = img.size # Get Dimensions
                    
                    
                  if width <= 256: # checks if the width is lower than 64 or if its 64

                    async with self.client.ses.get(url) as r:
                      if r.status in range(200, 299):

                        img = Image.open(BytesIO(await r.read()), mode='r') # Open Image URL
                        fixed_height = 560 # Height
                        height_percent = (fixed_height / float(img.size[1]))
                        width_size = int((float(img.size[0]) * float(height_percent)))
                        img_scaled = img.resize((width_size, fixed_height), Image.NEAREST) # Resizes the Image
                        b = BytesIO()
                        img_scaled.save(b, format=f'{img.format}') # Saves the Image
                        b_im = b.getvalue()
                        file = discord.File(filename=f'scaled.{img.format}', fp=BytesIO(b_im))

                        embed = discord.Embed(title='Scaled!', color=color)
                        embed.set_image(url=f'attachment://scaled.{img.format}')

                        await message.channel.send(embed = embed, file = file) # Sends the Image through embeds

                  else: # error if image is to big
                    embed = discord.Embed(
                      title='Error',
                      description='Image is too big. Must be **256x** or lower to scale images.',
                      color=error_color
                    )
                    await ctx.send(embed=embed)
        else: # error if replied message has no image
          await self.no_image(ctx)

      except: # error if command was executed but no replied messahe
        await self.no_reply(ctx)

    # rotate command
    @commands.command()
    async def rotate(self, ctx, degrees: int=None):
      pre = prefixes[str(ctx.guild.id)] # prefix
      try:
        # if <degrees> is left blank
        if degrees is None:
          embed = discord.Embed(
            title='Error',
            description=f'Enter Rotation Degrees.\nExample: ```{pre}rotate 90```',
            color=error_color
          )
          await ctx.send(embed=embed)
        # if its not left blank then...
        else:
          message = await ctx.channel.fetch_message(ctx.message.reference.message_id) # get replied message
          
          if len(message.attachments) > 0: # Checks if there are attachments to messages
            for file in message.attachments:
              for pic in pic_ext:
                
                if file.filename.endswith(pic):

                  attachment = message.attachments[0]

                  url = attachment.url # Get attachment url

                  async with self.client.ses.get(url) as r:
                    if r.status in range(200, 299):

                      img = Image.open(BytesIO(await r.read()), mode='r') # Open Image URL
                      img_rotated = img.rotate(angle=degrees) # Rotates Images to <degrees>
                      b = BytesIO()
                      img_rotated.save(b, format=f'{img.format}') # Saves the Image
                      b_im = b.getvalue()
                      file = discord.File(filename=f'rotated.{img.format}', fp=BytesIO(b_im))

                      embed = discord.Embed(
                        title='Rotated!',
                        color = color
                        )

                      embed.set_image(
                        url=f'attachment://rotated.{img.format}'
                        )

                      # await ctx.channel.trigger_typing()  # Bot is typing...
                      # await asyncio.sleep(2)

                      await ctx.send(embed = embed, file = file) # Sends the Image through embeds
          else: # error if theres no image in replied message
            await self.no_image(ctx)

      except: # error if command was executed but no replied message
        await self.no_reply(ctx)

    # size
    @commands.command()
    async def size(self, ctx):
      try:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id) # get replied message

        
        if len(message.attachments) > 0: # Checks if there are attachments to messages
          for file in message.attachments:
            for pic in pic_ext:
              
              if file.filename.endswith(pic):

                attachment = message.attachments[0]

                url = attachment.url # Get attachment url

                async with self.client.ses.get(url) as r:
                  if r.status in range(200, 299):
                    
                    img = Image.open(BytesIO(await r.read()), mode='r') # Open Image URL
                    width, height = img.size # Get Dimensions

                    embed = discord.Embed(
                      title='Image Dimensions by Pixels',
                      description=f'Width: **{width}**\nHeight: **{height}**',
                      color = color
                      )
                    await ctx.channel.trigger_typing()  # Bot is typing...
                    await asyncio.sleep(1)

                    await ctx.reply(embed=embed) # Sends the Dimensions through an embed
        else: # error if theres no image in replied message
          await self.no_image(ctx)

      except: # error if command was executed but no replied message
        await self.no_reply(ctx)
      

def setup(client):
    client.add_cog(Manipulation(client))