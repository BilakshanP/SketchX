from pyrogram.sync import compose

from Main import main_loop, clients

from Main.core.startup.post_startup import load_all_plugins

load_all_plugins(__file__)

async def main():
    await compose(clients[0] + clients[1])

if __name__ == "__main__":
    main_loop.run_until_complete(main())