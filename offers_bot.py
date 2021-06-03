from get_offers import get_offers
from dotenv import load_dotenv
import discord
import os
from time import sleep

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://store.steampowered.com/specials/"))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            # emoji1 = '\N{THUMBS UP SIGN}'
            # emoji2 = '\N{THUMBS DOWN SIGN}'
            # await message.add_reaction(emoji1)
            # await message.add_reaction(emoji2)
            return

        if message.content == 'exit':
            await client.close()

        if message.content in ['trending','most-popular','top-sellers','coming-soon']:
            channel = client.get_channel(839090488287952917)
            deals = get_offers(type=message.content)
            for id in range(0,len(deals['name'])):
                embed=discord.Embed(
                    title=deals['name'][id], 
                    url=deals['link'][id], 
                    description=f"Original Price (~~{deals['original_price'][id]}~~) Discount Price {deals['discount_price'][id]} **({deals['discount_pct'][id]})** "
                    )
                embed.set_image(url=deals['icon'][id])
                bot_message = await channel.send(embed=embed)
                emoji1 = '\N{THUMBS UP SIGN}'
                emoji2 = '\N{THUMBS DOWN SIGN}'
                await bot_message.add_reaction(emoji1)
                await bot_message.add_reaction(emoji2)

                sleep(2)


client = MyClient()
client.run(os.getenv("BOT_TOKEN"))