import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
import aiohttp

# colors
error_color = 0xff0000
color = 0xededed

# extensions
pic_ext = ['.jpg','.png','.jpeg']


class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.ses = aiohttp.ClientSession()

    @commands.Cog.listener()
    async def on_message(self, message):
      if len(message.attachments) > 0: # Checks if there are attachments to messages
        for file in message.attachments:
          for pic in pic_ext:

            if message.author == self.client.user: # Do not detect if the attachment was sent by any bot
              return
            if message.author.bot: return # if from a bot do not continue command
            
            if file.filename.endswith(pic):

              attachment = message.attachments[0]

              url = attachment.url # Get attachment url

              async with self.client.ses.get(url) as r:
                if r.status in range(200, 299):
                  
                  img = Image.open(BytesIO(await r.read()), mode='r') # Open Image URL
                  width, height = img.size # Get Dimensions
                  
                  
                  if width <= 64: # checks if the width is lower than 64
                    scale_emoji = '🔍'

                    await message.add_reaction(scale_emoji)

                    def check(reaction, user):
                      return user == message.author and str(reaction.emoji) in [scale_emoji]

                    scale_image = await self.client.wait_for("reaction_add", check=check)

                    if scale_image: # If user reacts to scale_emoji

                      img = Image.open(BytesIO(await r.read()), mode='r') # Open Image URL
                      fixed_height = 256 # Height
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

def setup(client):
    client.add_cog(Reaction(client))