from os import environ
from sys import argv
from dotenv import load_dotenv
from offers_bot import OffersBot

def main():

    load_dotenv()

    bot = OffersBot(environ['BOT_CHANNEL'], environ['BOT_TOKEN'])
    bot.run()

if __name__ == '__main__':
    main()