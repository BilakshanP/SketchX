from datetime import datetime, timedelta

from pyrogram.client import Client as _Client
from pyrogram.types.user_and_chats.user import User

from Main import Config
from Main.core.decorators.patches import monkeypatch # type: ignore

@monkeypatch(_Client)
class Client(_Client):
    """
    Type hinting help class for `pyrogram.client.Client`
    """
    def __init__(self, *args, **kwargs) -> None: # type: ignore
        super().__init__(*args, **kwargs) # type: ignore

        # for type hinting and auto completion of custom attributes:

        self.index: int
        self.client_type: str
        self.my_info: User|None
        self.last_info_update_time: datetime|None

    async def initialise_attributes(self, index: int, client_type: str):
        self.index = index
        self.client_type = client_type

        if Config.FAST_LOAD:
            self.my_info = None
            self.last_info_update_time = None
        else:
            self.my_info = await self.get_me()
            self.last_info_update_time = datetime.now()

    async def get_client(self, force: bool = False) -> User:
        if self.my_info is None or self.last_info_update_time is None or (datetime.now() - self.last_info_update_time) > timedelta(minutes=1) or force:
            self.my_info = await self.get_me()
            self.last_info_update_time = datetime.now()

        return self.my_info
    
    @property
    async def get_my_info(self, force: bool = False) -> User:
        return await self.get_client(force)