import os

from traceback import format_exc
from importlib import import_module

from pyrogram.client import Client

from Main import Config
from Main.core.helpers.logging_helper import (
    info as _info, error as _error, exception as _exception, empty as _empty
)

def load_all_plugins(file: str):
    """
    Pass __file__ to the argument.
    """
    for i in ["app", "bot"]:
        _empty()

        folder = os.path.join(
            os.path.dirname(file), "plugins", i
        )

        name: str = i.upper()

        _info(f"Loading [{name}] modules.")

        for plugin_file_name in os.listdir(folder):
            if plugin_file_name.endswith(".py"):

                if (plugin_file_name := plugin_file_name[:-3]) not in (Config.PLUGIN_NO_LOAD_APP if i == "app" else Config.PLUGIN_NO_LOAD_BOT):
                    _info(f"Loading module [{name}]: {plugin_file_name}.py", "    ")
    
                    try:
                        import_module(f".plugins.{i}.{plugin_file_name}", "Main")
                        _info(f"Loaded module [{name}]: {plugin_file_name}.py", "    ")
                    except BaseException as e:
                        _exception(f"Couldn't load module [{name}]: {plugin_file_name}.py - {e}", "    ")

                else:
                    _info(f"Skipping module [{name}]: {plugin_file_name}.py")
    
    _empty()

async def run_all_clients(clients: tuple[list[Client], list[Client]]):
    for num, name in enumerate(["APP", "BOT"]):
        length: int = len(clients[num])

        _info(f"Starting {name.lower()}s:")

        for index, app_or_bot in enumerate(clients[num]):

            try:
                await app_or_bot.start()
                _info(f"Started [{name}]: {index + 1}/{length}", "    ")

            except BaseException as e:

                if index:
                    _exception("", "    ")
                    _error(f"Couldn't start [{name}]: {num + 1}/{length}", "    ")
                else:
                    _exception("", "    ")
                    _error(f"Couldn't start main [{name}]. Exitting...", "    ")
                    quit()

        _info(f"Started all {name.lower()}s")

    _empty()