from pyrogram.filters import Filter

from Main import Config

from Main.core.types import Client, Message

async def sudo(_filter: Filter, client: Client, message: Message) -> bool:
    return (not Config.DISABLE_SUDO_USERS) and message and message.from_user and (message.from_user.id in Config.SUDO_USERS)