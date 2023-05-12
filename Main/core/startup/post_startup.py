import os
from importlib import import_module

from Main import Config
from Main.core.helpers.logging_helper import (
    info as _info, error as _error, warn as _warn, exception as _exception, empty as _empty
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

        for plugin_file_name in os.listdir(folder):
            if plugin_file_name.endswith(".py"):
                _info(f"Loading module [{name}]: {plugin_file_name}")

                try:
                    import_module(f".plugins.{i}.{plugin_file_name[:-3]}", "Main")
                    _info(f"Loaded module [{name}]: {plugin_file_name}")
                except BaseException as e:
                    _exception(f"Couldn't load module [{name}]: {plugin_file_name} - {e}", "    ")
                    