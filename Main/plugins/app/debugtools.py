from Main import Config

if Config.DEBUG:
    from pyrogram.client import Client

    from Main.core.types import Message
    from Main.core.decorators import app

    @app.on_command(
            "json",
            "Extracts JSON info of a pyorogram.types.Message object.",
            "json <reply to message>*"
    )
    async def json(client: Client, message: Message):
        print(message)
        await message.edit(f"`{message}`")
    
    @app.on_command(
            "args",
            "Returns message arguments.",
            "args -a -b -c --kwarg1=Hello --kwarg2=World !!!"
    )
    async def args(client: Client, message: Message):
        await message.edit(f"text: `{message.text}`\ninput: `{message.input}`\nargs: `{message.args}`\nkwargs: `{message.kwargs}`\ncommand: `{message.cmd}`")
    
    
    @app.on_command(
            "id",
            "Get IDs.",
            "id"
    )
    async def id(client: Client, message: Message):
        text = "\n".join(
            [
                f"Message ID: `{message.id}`",
                (f"Your ID: `{message.from_user.id}`" if message.from_user else f"Channel/Group ID: `{message.sender_chat.id}`"),
                (f"Your DC ID: `{message.from_user.dc_id}`\n" if message.from_user else f"Channel/Group ID: `{message.sender_chat.id}`"),
                f"Chat ID: `{message.chat.id}`",
                f"Chat DC ID: `{message.chat.dc_id}`"
            ]
        )
    
        if message.reply_to_message:
            text = "\n".join(
                [
                    text, "\n"
                    f"Replied Message ID: `{message.reply_to_message.id}`",
                    f"Replied User ID: `{message.reply_to_message.from_user.id}`", # or message.sender_chat.id}`",
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
    
    @app.on_command(
            "ss",
            "Exports your session string to your saved messages.",
            "ss"
    )
    async def get_session(client: Client, message: Message):
        session_string: str = await client.export_session_string()
    
        await client.send_message("me", f"**Your __session string__ is**: {session_string}")
        await message.edit("The session string has been sent to your Saved Messaged!")