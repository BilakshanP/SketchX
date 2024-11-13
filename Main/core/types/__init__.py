from typing import Callable, Awaitable

from .client import Client
from .message import Message

ClientOrNone = Message | None

MessageOrNone = Message | None
AsyncMessage = Awaitable[MessageOrNone]
AsyncMessageOrList = Awaitable[MessageOrNone | list[Message]]

Plugin = Callable[[Client, Message], MessageOrNone]
AsyncPlugin = Callable[[Client, Message], AsyncMessage]
AsyncPluginList = Callable[[Client, Message], AsyncMessageOrList]

HandlerDecoratorType = Callable[[AsyncPlugin], AsyncPlugin]
