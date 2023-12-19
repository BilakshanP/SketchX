from asyncio import get_event_loop
# from aiohttp import ClientSession as _ClientSession

from Main.core.configs import Config # type: ignore
from Main.core.data import HelpMenu

Menu = HelpMenu()

from Main.core.types import Client
from Main.core.startup import load_clients

main_loop = get_event_loop()
# aiohttp_session = _ClientSession()

clients: tuple[list[Client], list[Client]] = load_clients()

all_clients: list[Client] = clients[0] + clients[1]

all_apps: list[Client] = clients[0]
all_bots: list[Client] = clients[1]

main_app: Client = all_apps[0]
main_bot: Client = all_bots[0]

other_apps: list[Client] = all_apps[1:]
other_bots: list[Client] = all_bots[1:]