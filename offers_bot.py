from get_offers import get_offers
from dotenv import load_dotenv
import discord
import os
from time import sleep
import logging
from signal import signal, SIGINT, SIGTERM

load_dotenv()

logging.basicConfig(level=logging.INFO)

class OffersBot:

    def exit_handler(signal_received, frame):
        logging.info(f"[*] Signal received ({signal_received})....Exiting.")
        exit()

    def __init__(self, channel_name, bot_token):

        self.channel_name = channel_name
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

        @self.discord_bot.event
        async def on_message(message):
            
            if message.author.bot or str(message.channel) != self.channel_name:
                return

            if message.content is None:
                logging.error("[-] Empty message received.")
                return

            if message.content in ['trending','top-sellers','most-popular','coming-soon']:

                type = message.content

    def run(self):
        logging.info("[*] Now calling run()")
        self.discord_bot.run(self.token)
        logging.info("[*] Bot finished running.")