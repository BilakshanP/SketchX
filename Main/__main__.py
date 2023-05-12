import asyncio

from uvloop import install
from contextlib import closing, suppress

from pyrogram.sync import idle

from Main import all_clients, aiohttp_session
from Main.core.startup.post_startup import load_all_plugins

loop = asyncio.get_event_loop()

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

    with closing(loop):
        with suppress(asyncio.exceptions.CancelledError):
            loop.run_until_complete(main())

    loop.run_until_complete(asyncio.sleep(3.0))