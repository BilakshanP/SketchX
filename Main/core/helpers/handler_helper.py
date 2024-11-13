from typing import Callable, Any, Coroutine

from pyrogram.filters import Filter
from pyrogram.handlers.message_handler import MessageHandler

from Main import Config, all_apps, primary_app, all_bots, primary_bot
from Main.core.types import Client, Message
from Main.core.helpers.logging_helper import info as _info, warn as _warn

def add_app_handler(function_: Callable[[Client, Message], Coroutine[Any, Any, Message | None]], filters_: Filter, name: str, group: int = 0): 
    if name in Config.ALL_FUNC_PLUGIN_NO_LOAD_APP:
        if name in Config.MAIN_FUNC_PLUGIN_NO_LOAD_APP:
            _warn(f"Skipped [ALL APPS] {name}", "        ")
        else:
            primary_app.add_handler(
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

def add_bot_handler( function_: Callable[[Client, Message], Coroutine[Any, Any, Message | None]], filters_: Filter, name: str, group: int = 0): 
    if name in Config.ALL_FUNC_PLUGIN_NO_LOAD_BOT:
        if name in Config.MAIN_FUNC_PLUGIN_NO_LOAD_BOT:
            _warn(f"Skipped [ALL BOTS] {name}", "        ")
        else:
            primary_bot.add_handler(
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
