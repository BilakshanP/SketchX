from pyrogram.client import Client

from Main.core.decorators import bot
from Main.core.types import Message

@bot.on_command(["ping"], {"": ""}, False)
async def ping(client: Client, message: Message):
    await message.reply("Hello")