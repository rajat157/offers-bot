from get_offers import get_offers
from dotenv import load_dotenv
import discord
import os

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://store.steampowered.com/specials/"))
        channel = client.get_channel(846714712698650634)
        # await channel.send("Hello")
        deals = get_offers()
        deal = deals.get('top-sellers')
        await channel.send("Today's Deals!")
        for id in range(0,len(deal['name'])):
            embed=discord.Embed(
                title=deal['name'][id], 
                url=deal['link'][id], 
                description=f"Original Price (~~{deal['original_price'][id]}~~) Discount Price {deal['discount_price'][id]} **({deal['discount_pct'][id]})** "
                )
            embed.set_image(url=deal['icon'][id])
            await channel.send(embed=embed)
        await client.close()


        

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'exit':
            await client.close()

client = MyClient()
client.run(os.getenv("BOT_TOKEN"))