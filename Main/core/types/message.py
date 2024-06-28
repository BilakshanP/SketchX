from io import BytesIO
from datetime import datetime

from pyrogram.enums import ParseMode
from pyrogram.types import Message as _Message, MessageEntity, InlineKeyboardMarkup

from Main import Config
from Main.core.types import Client
# from Main.core.types.module import Arg, KwArg
from Main.core.errors.error import ClientIsNone
from Main.core.helpers.paste_helper import paste
from Main.core.helpers.logging_helper import debug as _debug, error as _error
from Main.core.decorators.patches import monkeypatch # type: ignore
from Main.core.helpers.type_helper import MessageHelper

@monkeypatch(_Message)
class Message(_Message):
    """
    Type hinting help class for `pyrogram.types.Message`
    """
    def __init__(self, *args, **kwargs) -> None: # type: ignore
        super().__init__(*args, **kwargs) # type: ignore

        # for type hinting and auto completion of custom attributes:

        self.input: str
        self.args: list[str]
        self.kwargs: dict[str, str]
        self.cmd: str

        self.chat_type: str

    async def initialise_attributes(self) -> tuple[str|None, list[str], dict[str, str], str, str]:
        self.input, self.args, self.kwargs, self.cmd = MessageHelper.process_input(self.text)

        chat_type = str(self.chat.type).lower()

        if chat_type.startswith("chattype"):
            self.chat_type = chat_type.split("chattype.")[1]


        return self.input, self.args, self.kwargs, self.cmd, self.chat_type
    
    @staticmethod
    async def from_raw_message(raw_message: _Message) -> "Message":
        raw_message.input, raw_message.args, raw_message.kwargs, raw_message.cmd, raw_message.chat_type = await Message.initialise_attributes(raw_message) # type: ignore
        return raw_message # type: ignore

    @staticmethod
    async def from_raw_message_or_none(raw_message: _Message|None) -> "Message|None":
        if raw_message:
            return await Message.from_raw_message(raw_message)

    
    async def edit_advance(
            self, text: str, parse_mode: ParseMode|None = None, entities: list[MessageEntity]|None = None, disable_web_page_preview: bool|None = None, reply_markup: InlineKeyboardMarkup|None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str|None = None, file_caption: str = "", delete_in: int|None = None, client: Client|None = None
        ) -> "Message|None":
        text = MessageHelper.markdown_to_raw_text(text)

        if as_paste or as_both or len(text) > 4096:
            bin, paste_link = await paste(text)
            result = await self.edit(f"**Pasted output to: __[{bin}]({paste_link})__**", disable_web_page_preview=True)

            if delete_in is not None:
                await result.delete()
                _debug(f"A message has been delete for a return type of 'Message' thus, 'NoneType' error might be raised.")
                return

            if not as_both:
                return await Message.from_raw_message(result)
    
        if as_file or as_both:
            if not file_name:
                file_name = "output.txt"
            
            file: BytesIO = BytesIO(text.encode())
            file.name = file_name
            
            result = await client.send_document(self.chat.id, file, reply_to_message_id=self.reply_to_message_id, caption=file_caption) # type: ignore
            await self.delete()

            return await Message.from_raw_message_or_none(result)

        return await Message.from_raw_message(await self.edit(text, parse_mode, entities, disable_web_page_preview, reply_markup)) # type: ignore
    
    async def reply_advance(
            self, text: str, quote: bool|None = None, parse_mode: ParseMode|None = None, entities: list[MessageEntity]|None = None, disable_web_page_preview: bool|None = None, disable_notification: bool|None = None, reply_to_message_id: int|None = None, schedule_date: datetime|None = None, protect_content: bool|None = None, reply_markup: InlineKeyboardMarkup|None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str|None = None, file_caption: str = "", delete_in: int|None = None, client: Client|None = None
        ) -> "Message|None":
        text = MessageHelper.markdown_to_raw_text(text)

        if as_paste or as_both or len(text) > 4096:
            bin, paste_link = await paste(text)
            result = await Message.from_raw_message(
                await self.reply(f"**Pasted output to: __[{bin}]({paste_link})__**", disable_web_page_preview=True, reply_to_message_id=reply_to_message_id) # type: ignore
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
            
            result = await client.send_document(self.chat.id, BytesIO(text.encode()), reply_to_message_id=self.reply_to_message_id, caption=file_caption) # type: ignore

            await self.delete()

            return await Message.from_raw_message(result) if result else result

        return await self.edit(text, parse_mode, entities, disable_web_page_preview, reply_markup) # type: ignore
    
    async def edit_or_reply(
            self, text: str, parse_mode: ParseMode|None = None, entities: list[MessageEntity]|None = None, disable_web_page_preview: bool|None = None, reply_markup: InlineKeyboardMarkup|None = None,
            quote: bool|None = None, disable_notification: bool|None = None, reply_to_message_id: int|None = None, schedule_date: datetime|None = None, protect_content: bool|None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str|None = None, file_caption: str = "", delete_in: int|None = None, client: Client|None = None
    ) -> "Message|None":
        if client is None:
            raise ClientIsNone

        if (fu_id := self.from_user.id) != (await client.get_client()).id and fu_id in Config.SUDO_USERS:
            return await self.reply_advance(text, quote, parse_mode, entities, disable_web_page_preview, disable_notification, reply_to_message_id, schedule_date, protect_content, reply_markup, as_paste, as_file, as_both, file_name, file_caption, delete_in, client)
        
        return await self.edit_advance(text, parse_mode, entities, disable_web_page_preview, reply_markup, as_paste, as_file, as_both, file_name, file_caption, delete_in, client)