from pyrogram.client import Client
from asyncio import get_event_loop as _loop
#from aiohttp import ClientSession as _ClientSession

main_loop = _loop()
#aiohttp_session = _ClientSession()

from Main.core.configs import Config
from Main.core.startup.pre_startup import load_clients

clients: tuple[list[Client], list[Client]] = load_clients()

apps: list[Client] = clients[0]
bots: list[Client] = clients[0]

main_app: Client = apps[0]
main_bot: Client = bots[0]