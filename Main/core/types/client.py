from datetime import datetime, timedelta

from pyrogram.client import Client as PyrogramClient
from pyrogram.types.user_and_chats.user import User

from Main import Config

class Client(PyrogramClient):
    """
    Type hinting help class for `pyrogram.client.Client`
    """

    async def initialise_attributes(self, index: int, client_type: str):
        self.index: int = index
        self.client_type: str = client_type
        self.my_info: User | None = None
        self.last_info_update_time: datetime | None = None

        if not Config.FAST_LOAD:
            self.my_info = await self.get_me()
            self.last_info_update_time = datetime.now()

    async def get_client(self, force: bool = False) -> User:
        if (
            force
            or self.my_info is None
            or self.last_info_update_time is None
            or (datetime.now() - self.last_info_update_time) > timedelta(seconds = Config.INFO_UPDATE_TIME_SEC or 60)
        ):
            self.my_info = await self.get_me()
            self.last_info_update_time = datetime.now()

        return self.my_info

    @property
    async def get_my_info(self, force: bool = False) -> User:
        return await self.get_client(force)

__all__ = ['datetime', 'timedelta', 'PyrogramClient', 'User', 'Config']