from typing import Callable

from Main import Config

from Main.core.types import Client, Message

async def sudo(function: Callable, client: Client, message: Message) -> bool: # type: ignore
    return not Config.DISABLE_SUDO_USERS and message and message.from_user and message.from_user.id in Config.SUDO_USERS