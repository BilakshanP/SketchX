import os

from importlib import import_module

from pyrogram.client import Client

from Main import Config
from Main.core.types import Client
from Main.core.helpers.logging_helper import info as _info, warn as _warn, error as _error, exception as _exception, empty as _empty

def load_all_local_plugins(file: str):
    """
    Pass `__file__` to it from the `__main__.py` file.
    """
    for i in ["app", "bot"]:
        _empty()

        folder = os.path.join(
            os.path.dirname(file), "plugins", i
        )

        name: str = i.upper()

        _info(f"Loading [{name}] modules.")

        for plugin_file_name in os.listdir(folder):
            if plugin_file_name.endswith(".py") and (plugin_file_name[:2] != "__" or plugin_file_name[-5:-3] != "__"):
                if (plugin_file_name := plugin_file_name[:-3]) not in (Config.ALL_MODULE_PLUGIN_NO_LOAD_APP):
                    _info(f"Loading module [{name}]: {plugin_file_name}.py", "    ")

                    try:
                        import_module(f".plugins.{i}.{plugin_file_name}", "Main")
                        _info(f"Loaded module  [{name}]: {plugin_file_name}.py", "    ")
                        _empty()

                    except Exception as e:
                        _exception(f"Couldn't load module [{name}]: {plugin_file_name}.py - {e}", "    ")

                else:
                    _warn(f"Skipping module [{name}]: {plugin_file_name}.py")

    _empty()

async def run_all_clients(clients: tuple[list[Client], list[Client]]):
    _info("Starting all clients.")

    for num, name in enumerate(["APP", "BOT"]):
        length: int = len(clients[num])

        _info(f"Starting {name.lower()}s:", "    ")

        for index, app_or_bot in enumerate(clients[num]):

            try:
                await app_or_bot.start()
                await app_or_bot.initialise_attributes(index, name.lower())

                _info(f"Started [{name}]: {index + 1}/{length}", "        ")

            except Exception as e:

                if index:
                    _exception(str(e), "    ")
                    _error(f"Couldn't start [{name}]: {num + 1}/{length}", "            ")
                else:
                    _exception(str(e), "    ")
                    _error(f"Couldn't start main [{name}]. Exitting...", "            ")
                    quit()

        _info(f"Started all {name.lower()}s", "    ")

        _empty()