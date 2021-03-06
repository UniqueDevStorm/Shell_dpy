from discord.ext import commands
from discord import Intents

from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

TOKEN = os.getenv('TOKEN')


class MyBOT(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=["/"],
            help_command=None,
            intents=Intents.all(),
        )

    async def on_ready(self):
        print(f'{str(self.user)} on Ready.')


bot = MyBOT()
bot.run(TOKEN)