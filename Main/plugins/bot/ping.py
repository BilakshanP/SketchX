from pyrogram.client import Client

from Main.core.decorators import bot
from Main.core.types.message import Message

@bot.on_command(["ping"], {"": ""}, False)
async def ping(client: Client, message: Message):
    print(message.text)