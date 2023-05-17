from asyncio import all_tasks
from pyrogram.client import Client

from Main import clients, main_loop, aiohttp_session

from Main.core.helpers.logging_helper import (
    info as _info, error as _error, exception as _exception, empty as _empty
)

async def close_all_clients(clients: tuple[list[Client], list[Client]]):
    _empty()

    for num, name in enumerate(["APP", "BOT"]):
        length: int = len(clients[num])

        for index, app_or_bot in enumerate(clients[num]):
            _info(f"Stopping {name.lower()}s:")

            try:
                await app_or_bot.stop()
                _info(f"Stopped [{name}]: {index + 1}/{length}", "    ")

            except BaseException as e:
                _exception(str(e))

                if index:
                    _error(f"Couldn't stop [{name}] properly: {num + 1}/{length}", "    ")
                else:
                    _error(f"Couldn't stop main [{name}] properly.", "    ")

        _info(f"Stopped all {name.lower()}s")

async def exit():
    await close_all_clients(clients)
    await aiohttp_session.close()

    for task in all_tasks():
        task.cancel()