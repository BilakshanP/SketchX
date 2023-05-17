from pyrogram.types import Message as _Message

from Main.core.decorators.others import monkeypatch
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

    async def initialise_attributes(self):
        self.input, self.args, self.kwargs, self.cmd = MessageHelper.process_input(self.text)
        return self.input, self.args, self.kwargs, self.cmd