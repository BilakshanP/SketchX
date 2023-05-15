from pyrogram.types import Message as _Message

from Main.core.decorators.others import monkeypatch

@monkeypatch(_Message)
def something():
    return "Something"