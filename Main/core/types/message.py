from io import BytesIO
from typing import Any, cast
from datetime import datetime

from pyrogram.enums import ParseMode
from pyrogram.types import Message as PyrogramMessage, MessageEntity, InlineKeyboardMarkup

from Main import Config
from Main.core.types import Client
from Main.core.errors import ClientIsNone
from Main.core.helpers.paste_helper import paste
from Main.core.helpers.logging_helper import debug as _debug, error as _error
from Main.core.helpers.type_helper import MessageHelper

class Message(PyrogramMessage):
    """
    Type hinting help class for `pyrogram.types.Message`
    """

    async def initialise_attributes(self) -> tuple[str | None, list[str], dict[str, str], str, str]:
        self.input: str
        self.args: list[str]
        self.kwargs: dict[str, str]
        self.cmd: str

        self.chat_type: str
        self.input, self.args, self.kwargs, self.cmd = MessageHelper.process_input(self.text)

        chat_type = str(self.chat.type).lower()

        if chat_type.startswith("chattype"):
            self.chat_type = chat_type.split("chattype.")[1]


        return self.input, self.args, self.kwargs, self.cmd, self.chat_type
    
    @staticmethod
    async def from_raw_message(raw_message: PyrogramMessage) -> 'Message':
        obj_data: dict[str, Any] = raw_message.__dict__

        del obj_data['_client']

        message = Message(**raw_message.__dict__)
        await message.initialise_attributes()
        return message

    @staticmethod
    async def from_raw_message_or_none(raw_message: PyrogramMessage | None) -> "Message | None":
        if raw_message:
            return await Message.from_raw_message(raw_message)

    
    async def edit_advance(
            self, text: str, parse_mode: ParseMode | None = None, entities: list[MessageEntity] = [], disable_web_page_preview: bool = False, reply_markup: InlineKeyboardMarkup | None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str | None = None, file_caption: str = "", delete_in: int | None = None, client: Client | None = None
        ) -> 'Message|None':
        text = MessageHelper.markdown_to_raw_text(text)

        if as_paste or as_both or len(text) > 4096:
            bin, paste_link = await paste(text)
            result = await self.edit(f"**Pasted output to: __[{bin}]({paste_link})__**", disable_web_page_preview=True)

            if delete_in is not None:
                await result.delete()
                _debug(f"The message has been deleted for a return type of 'Message' thus, 'NoneType' error might be raised.")
                return

            if not as_both:
                return await Message.from_raw_message(result)
    
        if as_file or as_both:
            if not file_name:
                file_name = "output.txt"
            
            file: BytesIO = BytesIO(text.encode())
            file.name = file_name

            if client is not None:
                result = await client.send_document(self.chat.id, file, reply_to_message_id=self.reply_to_message_id, caption=file_caption) # type: ignore - method lacks proper type hints
                await self.delete()
                return await Message.from_raw_message_or_none(result)
            
            raise ClientIsNone()

        return await Message.from_raw_message(await self.edit(text, parse_mode, entities, disable_web_page_preview, reply_markup=cast(InlineKeyboardMarkup, reply_markup))) 
    
    async def reply_advance(
            self, text: str, quote: bool | None = None, parse_mode: ParseMode | None = None, entities: list[MessageEntity] = [], disable_web_page_preview: bool = False, disable_notification: bool | None = None, reply_to_message_id: int | None = None, schedule_date: datetime | None = None, protect_content: bool | None = None, reply_markup: InlineKeyboardMarkup | None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str | None = None, file_caption: str = "", delete_in: int | None = None, client: Client | None = None
        ) -> 'Message|None':
        text = MessageHelper.markdown_to_raw_text(text)

        if as_paste or as_both or len(text) > 4096:
            bin, paste_link = await paste(text)
            result = await Message.from_raw_message(
                await self.reply(f"**Pasted output to: __[{bin}]({paste_link})__**", disable_web_page_preview=True, reply_to_message_id = cast(int, reply_to_message_id)) # type: ignore - method lacks proper type hints
            )

            if not as_both:
                return result
    
        if as_file or as_both:
            if not file_name:
                file_name = "output.txt"
            
            if client is None:
                result = await self.edit("Couldn't upload the text as document. As client paramater is set to None.")
                _error(f"Couldn't upload the text as document. As client paramater is set to None. File: {self.__module__}")
                return await Message.from_raw_message(result)
            
            result = await client.send_document(self.chat.id, BytesIO(text.encode()), reply_to_message_id=self.reply_to_message_id, caption=file_caption) # type: ignore - method lacks proper type hints

            await self.delete()

            return await Message.from_raw_message(result) if result else result
    
        message = await self.edit(text, parse_mode, entities, disable_web_page_preview, reply_markup=cast(InlineKeyboardMarkup, reply_markup))

        return await Message.from_raw_message(message)
    
    async def edit_or_reply(
            self, text: str, parse_mode: ParseMode | None = None, entities: list[MessageEntity] = [], disable_web_page_preview: bool = False, reply_markup: InlineKeyboardMarkup | None = None,
            quote: bool | None = None, disable_notification: bool | None = None, reply_to_message_id: int | None = None, schedule_date: datetime | None = None, protect_content: bool | None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str | None = None, file_caption: str = "", delete_in: int | None = None, client: Client | None = None
    ) -> 'Message|None':
        if client is None:
            raise ClientIsNone

        if (fu_id := self.from_user.id) != (await client.get_client()).id and fu_id in Config.SUDO_USERS:
            return await self.reply_advance(text, quote, parse_mode, entities, disable_web_page_preview, disable_notification, reply_to_message_id, schedule_date, protect_content, reply_markup, as_paste, as_file, as_both, file_name, file_caption, delete_in, client)
        
        return await self.edit_advance(text, parse_mode, entities, disable_web_page_preview, reply_markup, as_paste, as_file, as_both, file_name, file_caption, delete_in, client)