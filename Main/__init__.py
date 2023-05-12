from pyrogram.client import Client

from aiohttp import ClientSession as _ClientSession

aiohttp_session = _ClientSession()

from Main.core.configs import Config
from Main.core.startup.pre_startup import load_clients

clients: tuple[list[Client], list[Client]] = load_clients()

all_clients: list[Client] = clients[0] + clients[1]

apps: list[Client] = clients[0]
bots: list[Client] = clients[0]