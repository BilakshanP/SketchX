from asyncio import get_event_loop

from Main.core.config import Config
from Main.core.data import HelpMenu
from Main.core.types import Client
from Main.core.startup.pre_startup import load_clients

Menu = HelpMenu()
main_loop = get_event_loop()
clients: tuple[list[Client], list[Client]] = load_clients()

all_clients: list[Client] = clients[0] + clients[1]

all_apps: list[Client] = clients[0]
all_bots: list[Client] = clients[1]

primary_app: Client = all_apps[0]
primary_bot: Client = all_bots[0]

secondary_apps: list[Client] = all_apps[1:]
secondary_bots: list[Client] = all_bots[1:]

# Exports
__all__ = [
    'Config',
    'Menu',
    'Client',
    'main_loop',
    'all_clients',
    'all_apps',
    'all_bots',
    'primary_app',
    'primary_bot',
    'secondary_apps',
    'secondary_bots'
]