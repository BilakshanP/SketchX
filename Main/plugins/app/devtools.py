from os import execle, environ
from sys import executable

from pyrogram import filters
from pyrogram.client import Client

from Main.core.types.message import Message
from Main.core.decorators import app

@app.on_command(["restart"])
async def restart(client: Client, message: Message):
    await message.edit("Restarting...")

    args: list[str] = [executable, "-m", "Main"]
    execle(executable, *args, environ)