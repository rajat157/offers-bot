# OffersBot

OffersBot is a Discord bot which fetches the list of games on discount from the Steam store.

## Installation

### Linux
1) python -m venv virt-env
2) source virt-env/bin/activate
3) pip install discord.py requests beautifulsoup4
4) git clone https://github.com/rajat157/offers-bot.git

## Usage
```bash
cd offers-bot
vim .env
BOT_TOKEN="Add your bot token here"
BOT_CHANNEL="Add channel ID here"

# Run the offers bot
python run.py
```
### Optional
```bash
# Set a cronjob to run this bot on regular intervals.
# Example:
crontab -e
0 17 * * *    cd offers-bot && python run.py  # This will run the bot at 5 PM, everyday.
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
