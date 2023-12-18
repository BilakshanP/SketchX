from pyrogram.enums.chat_type import ChatType
from pyrogram.types import Message as _Message

from Main.core.decorators.patches import monkeypatch
from Main.core.helpers.type_helper import MessageHelper


@monkeypatch(_Message)
class Message(_Message):
    """
    Type hinting help class for `pyrogram.types.Message`
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

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