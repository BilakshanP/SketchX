from uvloop import install
from contextlib import closing, suppress
from asyncio.exceptions import CancelledError

from pyrogram.sync import idle

from Main import clients, main_loop
from Main.core.startup.post_startup import load_all_local_plugins, run_all_clients
from Main.core.shutdown import complete_exit

load_all_local_plugins(__file__)

async def main():
    await run_all_clients(clients)
    await idle()
    await complete_exit()

if __name__ == "__main__":
    install()

    with closing(main_loop) as loop:
        with suppress(CancelledError):
            loop.run_until_complete(main())