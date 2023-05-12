import asyncio

from uvloop import install
from contextlib import closing, suppress

from pyrogram.sync import idle

from Main import all_clients, main_loop, aiohttp_session
from Main.core.startup.post_startup import load_all_plugins

load_all_plugins(__file__)

async def main():
    for client in all_clients:
        await client.start()

    await idle()

    for client in all_clients:
        await client.stop()

    await aiohttp_session.close()

    for task in asyncio.all_tasks():
        task.cancel()

if __name__ == "__main__":
    install()

    with closing(main_loop):
        with suppress(asyncio.exceptions.CancelledError):
            main_loop.run_until_complete(main())

        main_loop.run_until_complete(asyncio.sleep(3.0))