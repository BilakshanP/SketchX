from Main import Config

if Config.DEBUG:
    from pyrogram.types import User, Chat

    from Main.core.types import Message, Client
    from Main.core.decorators import app

    @app.on_command(
            "json",
            "Extracts JSON info of a pyorogram.types.Message object.",
            "json <reply to message>*"
    )
    async def json(client: Client, message: Message):
        print(f"{message.text} {message.input} {message.args} {message.kwargs} {message.cmd}")
        await message.edit_advance(f"`{message}`", as_file = 'f' in message.args, client=client)

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
    async def id2(client: Client, message: Message):
        def format_user_info(user: User) -> list[str]:
            return [
                f"Replied User ID: `{user.id}`",
                f"Replied User DC ID: `{user.dc_id}`"
            ]

        def format_chat_info(chat: Chat) -> list[str]:
            return [
                f"Replied Chat ID: `{chat.id}`",
                f"Replied Chat DC ID: `{chat.dc_id}`"
            ]
    
        def format_dc_ids(dc_id: int) -> str:
            dc_ids: list[str] = [
                '',
                "Miami FL, USA",
                "Amsterdam, NL",
                "Miami FL, USA",
                "Amsterdam, NL",
                "Singapore, SG",
            ]

            return f"{dc_id}: {dc_ids[dc_id]}"

        chat_ids: list[str] = [
            f"Chat ID: `{message.chat.id}`",
            f"Chat DC ID: `{format_dc_ids(message.chat.dc_id)}`\n",
            f"Message ID: `{message.id}`",
            f"Your ID: `{message.from_user.id}`" if message.from_user else f"Channel/Group ID: `{message.sender_chat.id}`",
            f"Your DC ID: `{format_dc_ids(message.from_user.dc_id)}`" if message.from_user else f"Channel/Group ID: `{format_dc_ids(message.sender_chat.dc_id)}`"
        ]

        if (rtm := message.reply_to_message):
            chat_ids.append(f"\nReplied Message ID: `{rtm.id}`")

            if (user := rtm.from_user):
                chat_ids.extend(format_user_info(user))
            else:
                chat_ids.extend(format_chat_info(rtm.sender_chat))

            if rtm.forward_date and (ffc := rtm.forward_from_chat):
                chat_ids.extend(
                [
                    f"\nForwarded Message ID: `{rtm.forward_from_message_id}`",
                    f"Forwarded from Chat ID: `{ffc.id}`",
                    f"Forwarded from Chat DC ID: `{format_dc_ids(ffc.dc_id)}`",
                ]
            )

            text: str = "**__" + "\n".join(chat_ids) + "__**"
            await message.edit(text)

    @app.on_command(
            "ss",
            "Exports your session string to your saved messages.",
            "ss"
    )
    async def get_session(client: Client, message: Message):
        session_string: str = await client.export_session_string()

        await client.send_message("me", f"**Your __session string__ is**: `{session_string}`")
        await message.edit("The session string has been sent to your Saved Messages!")