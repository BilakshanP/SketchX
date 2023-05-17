from io import BytesIO
from typing import Optional, List
from traceback import format_exc

from pyrogram.enums import ParseMode
from pyrogram.types import Message, MessageEntity, InlineKeyboardMarkup
from pyrogram.client import Client

from Main import Config
from Main.core.helpers.paste_helper import paste
from Main.core.helpers.logging_helper import exception as _exception
from Main.core.helpers.regex_helper import Compiled

async def edit(
        client: Client,
        message: Message,
        text: str,
        parse_mode: Optional[ParseMode] = ParseMode.MARKDOWN,
        entities: List[MessageEntity] = None, # type: ignore
        disable_web_page_preview: bool = True,
        reply_markup: InlineKeyboardMarkup = None # type: ignore
    ) -> Message:
    if len(text) > 4096:
        try:
            text = f"Text too long! Pasted on [Nekobin]({await paste(text)})."
        except BaseException as e1:
            traceback = format_exc().replace("\n", "\n    ")

            _exception(
                    traceback, silence = not Config.DEBUG
                )

            await message.edit(f"Text too long! Trying to send it as a file.")

            msg: Optional[Message] = await client.send_document(
                    message.chat.id, caption = f"Output of [Command](https://t.me/c/{message.chat.id}/{message.id}).",
                    file_name = "edit.txt", document = BytesIO(
                            text.replace("\\n", "\n").replace("\\\"", "\"").strip("`").encode()
                    ), 
                )

            if msg:
                return await message.edit(f"Command [result](https://t.me/c/{message.chat.id}/{msg.id}).")

            else:
                return await message.edit(f"Couldn't send the file! Try again or check your permissions.")

    return await message.edit(text, parse_mode, entities, disable_web_page_preview, reply_markup)