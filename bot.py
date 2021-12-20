"""
CFRankListBot: A Telegram bot for the CF Ranking List.

Commands:
/getrank - Fetch the latest CF rounds ranking list.
/about - About the bot.
/help - Help.
"""

from bot import commands
import os


token = os.environ.get('TOKEN')

commands.init(token)
