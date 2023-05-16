from pyrogram.types import Message as _Message

from Main.core.decorators.others import monkeypatch
from Main.core.helpers.type_helper import MessageHelper


@monkeypatch(_Message)
class Message(_Message):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.raw_text = self.text
        