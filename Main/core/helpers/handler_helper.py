from typing import Callable

from pyrogram.filters import Filter
from pyrogram.handlers.message_handler import MessageHandler

from Main import Config, all_apps, main_app, all_bots, main_bot
from Main.core.helpers.logging_helper import (
        info as _info, warn as _warn, exception as _exception, debug as _debug
    )

def add_app_handler( function_: Callable, filters_: Filter, name: str, group: int = 0):
    if name in Config.ALL_FUNC_PLUGIN_NO_LOAD_APP:
        if name in Config.MAIN_FUNC_PLUGIN_NO_LOAD_APP:
            _warn(f"Skipped [ALL APPS] {name}", "        ")
        else:
            main_app.add_handler(
                MessageHandler(
                    function_,
                    filters_
                ),
                group = group
            )

            _info(f"Added [MAIN APP]: {name}", "        ")
    
    else:
        for app in all_apps:
            app.add_handler(
                MessageHandler(
                    function_,
                    filters_
                ),
                group = group
            )

        _info(f"Added [ALL APPS]: {name}", "        ")

def add_bot_handler( function_: Callable, filters_: Filter, name: str, group: int = 0):
    if name in Config.ALL_FUNC_PLUGIN_NO_LOAD_BOT:
        if name in Config.MAIN_FUNC_PLUGIN_NO_LOAD_BOT:
            _warn(f"Skipped [ALL BOTS] {name}", "        ")
        else:
            main_bot.add_handler(
                MessageHandler(
                    function_,
                    filters_
                ),
                group = group
            )

            _info(f"Added [MAIN BOT]: {name}", "        ")
    
    else:
        for bot in all_bots:
            bot.add_handler(
                MessageHandler(
                    function_,
                    filters_
                ),
                group = group
            )

        _info(f"Added [ALL BOTS]: {name}", "        ")
