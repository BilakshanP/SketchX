from typing import Callable

from Main import Config

from Main.core.types.client import Client
from Main.core.types.message import Message

async def sudo(function: Callable, client: Client, message: Message) -> bool:
    return not Config.DISABLE_SUDO_USERS and message and message.from_user and message.from_user.id in Config.SUDO_USERS