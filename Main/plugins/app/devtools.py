from os import execle, environ
from sys import executable
from pyrogram import filters

from pyrogram.types import Message
from pyrogram.client import Client

from Main.core.decorators import app

@app.on_command(["json"])
async def json(client: Client, message: Message):
    await message.edit(f"{message}")

@app.on_command(["id"])
async def id(client: Client, message: Message):
    text: str = '**__\n'.join(
            [
                f"Message ID: {message.id}",
                f"Your ID: {message.from_user.id}",
                f"Your DC ID: {message.from_user.dc_id}",
                f"\nChat ID: {message.chat.id}",
                f"Chat DC ID: {message.chat.dc_id}",
            ]
        ) + "" if not message.reply_to_message else '\n'.join(
            [
                f"\n\nReply to Message ID: {message.reply_to_message.id}",
                f"Replied User ID: {message.reply_to_message.from_user.id}",
                f"Replied User DC ID: {message.reply_to_message.from_user.dc_id}__**"
            ]
        )
    
    print(
            f"Message ID: {message.id}",
            f"Your ID: {message.from_user.id}",
            f"Your DC ID: {message.from_user.dc_id}",
            f"\nChat ID: {message.chat.id}",
            f"Chat DC ID: {message.chat.dc_id}",
            f"\n\nReply to Message ID: {message.reply_to_message.id}",
            f"Replied User ID: {message.reply_to_message.from_user.id}",
            f"Replied User DC ID: {message.reply_to_message.from_user.dc_id}",
            sep ="\n"
        )

    await message.edit(text)

@app.on_command(["ss"])
async def get_session(client: Client, message: Message):
    session_string: str = await client.export_session_string()

    await client.send_message("me", f"**Your __session string__ is**: {session_string}")
    await message.edit("The session string has been sent to your Saved Messaged!")

@app.on_command(["restart"])
async def restart(client: Client, message: Message):
    await message.edit("Restarting...")

    args: list[str] = [executable, "-m", "Main"]
    execle(executable, *args, environ)