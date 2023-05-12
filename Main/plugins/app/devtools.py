from os import execle, environ
from sys import executable
from pyrogram import filters

from pyrogram.types import Message
from pyrogram.client import Client

from Main import main_loop
from Main.core.decorators import app

@app.on_command(["json"])
async def json(client: Client, message: Message):
    await message.edit(f"`{message}`")

@app.on_command(["ss"])
async def get_session(client: Client, message: Message):
    session_string: str = await client.export_session_string()

    await client.send_message("me", f"**Your __session string__ is**: `{session_string}`")
    await message.edit("The session string has been sent to your Saved Messaged!")

@app.on_command(["restart"])
async def restart(client: Client, message: Message):
    await message.edit("Restarting...")

    args = [executable, "-m", "Main"]
    execle(executable, *args, environ)