from get_offers import get_offers
from dotenv import load_dotenv
import discord
import os
from time import sleep
import logging
from signal import signal, SIGINT, SIGTERM
import subprocess as sp

logging.basicConfig(level=logging.INFO)

class OffersBot:

    def exit_handler(signal_received, frame):
        logging.info(f"[*] Signal received ({signal_received})....Exiting.")
        exit()

    def __init__(self, channel_id, bot_token):

        self.channel_id = int(channel_id)
        self.token = bot_token

        # Set up Discord
        logging.info("[*] Initializing Discord bot...")
        self.discord_bot = discord.AutoShardedClient()
        self.bot_events()
        logging.info("[+] Done initializing Discord bot.")
        logging.info("[+] Exiting __init__ function.")

        logging.info("[*] Setting up signal handlers")
        signal(SIGINT, self.exit_handler)
        signal(SIGTERM, self.exit_handler)

    def bot_events(self):

        logging.info("[+] Setting up Discord events")

        @self.discord_bot.event
        async def on_ready():

            logging.info("[+] Bot on_ready. Connected to Discord")
            logging.info("[*] Name: {}".format(self.discord_bot.user.name))
            logging.info("[*] ID: {}".format(self.discord_bot.user.id))
            await self.discord_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://store.steampowered.com/specials/"))
            await get_deals(self.channel_id)

        @self.discord_bot.event
        async def on_message(message):
            
            if message.author.bot or message.channel.id != self.channel_id:
                return

            if message.content is None:
                logging.error("[-] Empty message received.")
                return

        @self.discord_bot.event
        async def get_deals(channel_id):
            channel = await self.discord_bot.fetch_channel(channel_id)
            deal_type = "top-sellers"
            deals = get_offers(type=deal_type)
            
            embed=discord.Embed(
                title="What's on Steam today",
                url = "https://store.steampowered.com/specials/"
                )
            for id in range(0,len(deals['name'])):
                embed.add_field(
                    name=deals['name'][id],
                    value=f"Original Price (~~{deals['original_price'][id]}~~) Discount Price {deals['discount_price'][id]} **({deals['discount_pct'][id]})**\n{deals['link'][id]}",
                    # value = deals['link'][id],
                    inline=False
                )
            await channel.send(embed=embed)
                    

    def run(self):
        logging.info("[*] Now calling run()")
        self.discord_bot.run(self.token)
        logging.info("[*] Bot finished running.")