from asyncio import get_event_loop
from aiohttp import ClientSession as _ClientSession

from pyrogram.client import Client

from Main.core.configs import Config
from Main.core.startup.pre_startup import load_clients

main_loop = get_event_loop()
aiohttp_session = _ClientSession()

clients: tuple[list[Client], list[Client]] = load_clients()

all_clients: list[Client] = clients[0] + clients[1]

apps: list[Client] = clients[0]
bots: list[Client] = clients[0]