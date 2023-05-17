from os import execle, environ
from sys import executable
from pyrogram import filters

from pyrogram.client import Client

from Main.core.types.message import Message
from Main.core.decorators import app


@app.on_command(["json"])
async def json(client: Client, message: Message):
    print(message)
    await message.edit(f"`{message}`")

@app.on_command(["args"])
async def test_json(client: Client, message: Message):
    await message.edit(f"text: `{message.text}`\ninput: `{message.input}`\nargs: `{message.args}`\nkwargs: `{message.kwargs}`\ncommad: `{message.cmd}`")


@app.on_command(["id"])
async def id(client: Client, message: Message):
    text = "\n".join(
        [
            f"Message ID: `{message.id}`",
            f"Your ID: `{message.from_user.id}`",
            f"Your DC ID: `{message.from_user.dc_id}`\n",
            f"Chat ID: `{message.chat.id}`",
            f"Chat DC ID: `{message.chat.dc_id}`"
        ]
    )

    if message.reply_to_message:
        text = "\n".join(
            [
                text, "\n"
                f"Replied Message ID: `{message.reply_to_message.id}`",
                f"Replied User ID: `{message.reply_to_message.from_user.id}`" # or message.sender_chat.id}`",
                f"Replied User DC ID: `{message.reply_to_message.from_user.dc_id}`" # or message.sender_chat.dc_id}`"
            ]
        )
    
    # To be fixed
    #
    # if message.forward_from_chat:
    #     text = "\n".join(
    #         [
    #             text, "\n",
    #             f"Forwarded from Message ID: `{message.forward_from_message_id}`",
    #             f"Forwarded from ID: `{message.forward_from_chat.id}`"
    #             f"Forwarded from DC ID:`{message.forward_from_chat.dc_id}`"
    #         ]
    #     )

    await message.edit("**__" + text + "__**")

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

"""
 "\n\n" +
            f"Replied Message ID: {message.reply_to_message.id}\n" +
            f"Replied User ID: {message.reply_to_message.from_user.id}\n" +
            f"Replied User DC ID: {message.reply_to_message.from_user.dc_id}\n"
        ) if message.reply_to_message else ""
"""