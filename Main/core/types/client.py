from datetime import datetime

from pyrogram.client import Client as _Client
from pyrogram.types.user_and_chats.user import User

from Main import Config
from Main.core.decorators.patches import monkeypatch

@monkeypatch(_Client)
class Client(_Client):
    """
    Type hinting help class for `pyrogram.client.Client`
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

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

    async def get_client(self) -> User:
        self.my_info = await self.get_me()
        self.last_update_time = datetime.now()

        return self.my_info
