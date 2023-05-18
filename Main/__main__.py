import asyncio

from uvloop import install
from contextlib import closing, suppress

from pyrogram.sync import idle

from Main import clients, main_loop, aiohttp_session
from Main.core.startup.post_startup import load_all_local_plugins, run_all_clients
from Main.core.shutdown.shutdown import close_all_clients

load_all_local_plugins(__file__)

async def main():
    await run_all_clients(clients)

    await idle()

    await close_all_clients(clients)

    await aiohttp_session.close()

    for task in asyncio.all_tasks():
        task.cancel()

if __name__ == "__main__":
    install()

    with closing(main_loop):
        with suppress(asyncio.exceptions.CancelledError):
            main_loop.run_until_complete(main())