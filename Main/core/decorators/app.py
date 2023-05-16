from traceback import format_exc

from pyrogram import filters, StopPropagation, ContinuePropagation
from pyrogram.types import Message
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler

from Main import Config, apps
#from Main.core.helpers.paste_helper import paste as _paste
from Main.core.helpers.logging_helper import (
        info as _info, error as _error, warn as _warn, exception as _exception, debug as _debug
    )

def add_app_handler(filters_, function_, name):
    for app in apps:
        app.add_handler(
            MessageHandler(
                function_,
                filters_
            ),
            group = 0
        )

    _info(f"Added {name}", append = "    ")

def on_command(
        command: list = ["example"],
        command_help: dict = {
            "help": "This ia an example help.",
            "example": f"{Config.COMMAND_HANDLER}example"
        },
        admin_only: bool = False
):
    base_filters = (
        filters.outgoing & filters.text & filters.command(command, Config.COMMAND_HANDLER)
    )

    def decorator(func):
        async def wrapper(client: Client, message: Message):
            _debug(f"Called {func.__name__}")

            try:
                await func(client, message)
            except StopPropagation:
                raise StopPropagation
            except ContinuePropagation:
                raise ContinuePropagation
            #except MessageTooLong:
            #    try:
            #        await message.edit(await _paste("what"))
            #    except:
            #        print(await _paste("what"))
            except BaseException as e1:
                try:
                    await message.edit("Something went wrong, check logs.")

                    traceback = format_exc().replace("\n", "\n    ")

                    _exception(
                        f"Module: {func.__module__} - Function: {func.__name__}: {e1}"
                    )
                    _exception(
                        traceback, silence = not Config.DEBUG
                    )
                except BaseException as e2:
                    traceback = format_exc().replace("\n", "\n    ")

                    _error("An exception occured while handling of another exception: ")

                    _exception(
                        f"Module: {func.__module__} - Function: {func.__name__}: {e2} during {e1}"
                    )

                    _exception(
                        traceback, silence = not Config.DEBUG
                    )
        
        add_app_handler(base_filters, wrapper, func.__name__)
        return wrapper
    return decorator