from io import BytesIO
from typing import Optional, List

from pyrogram.enums import ParseMode
from pyrogram.types import Message as _Message, MessageEntity, InlineKeyboardMarkup

from Main.core.types.client import Client
from Main.core.helpers.paste_helper import paste
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
    
    async def edit_advance(
            self, text: str, parse_mode: Optional[ParseMode] = None, entities: List[MessageEntity]|None = None, disable_web_page_preview: bool|None = None, reply_markup: InlineKeyboardMarkup|None = None,
            as_paste: bool = False, as_file: bool = False, as_both: bool = False, file_name: str|None = None, file_caption: str = "", reply_to_message_id: int|None = None, delete_in: int|None = None, client: Client|None = None
        ) -> "Message":
        text = MessageHelper.markdown_to_raw_text(text)

        if as_paste or as_both or len(text) > 4096:
            bin, paste_link = await paste(text)
            result = await self.edit(f"**Pasted output to: __[{bin}]({paste_link})__**", disable_web_page_preview=True) # type: ignore

            if not as_both:
                return result # type: ignore
    
        if as_file or as_both:
            if not file_name:
                file_name = "output.txt"
            
            result = await client.send_document(self.chat.id, BytesIO(text.encode()), reply_to_message_id=self.reply_to_message_id, caption=file_caption, disable_web_page_preview=True) # type: ignore
            await self.delete()

            return result # type: ignore

        return await self.edit(text, parse_mode, entities, disable_web_page_preview, reply_markup) # type: ignore
    
    async def edit_or_reply(self) -> None:
        raise NotImplementedError