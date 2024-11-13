from asyncio import all_tasks

from Main import clients
from Main.core.types import Client
from Main.core.helpers.paste_helper import Paste
from Main.core.helpers.logging_helper import info as _info, error as _error, exception as _exception, empty as _empty

async def close_all_clients(clients: tuple[list[Client], list[Client]]):
    _empty()

    for num, name in enumerate(["APP", "BOT"]):
        length: int = len(clients[num])

        _info(f"Stopping {name.lower()}s:")

        for index, app_or_bot in enumerate(clients[num]):
            try:
                await app_or_bot.stop()
                _info(f"Stopped [{name}]: {index + 1}/{length}", "    ")

            except Exception as e:
                _exception(str(e))

                if index:
                    _error(f"Couldn't stop [{name}] properly: {num + 1}/{length}", "    ")
                else:
                    _error(f"Couldn't stop main [{name}] properly.", "    ")

        _info(f"Stopped all {name.lower()}s")

async def complete_exit():
    await close_all_clients(clients)
    await Paste.aiohttp_session.close()

    for task in all_tasks():
        task.cancel()