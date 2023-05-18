from traceback import format_exc

from pyrogram import filters, StopPropagation, ContinuePropagation
from pyrogram.client import Client

from Main import Config
from Main.core.types.message import Message
from Main.core.helpers.handler_helper import add_bot_handler
from Main.core.helpers.logging_helper import (
        error as _error, warn as _warn, exception as _exception, debug as _debug
    )


def on_command(
        command: list = ["example"],
        command_help: dict = {
            "help": "This ia an example help.",
            "example": f"{Config.COMMAND_HANLDER_BOT}example"
        },
        admin_only: bool = False
):
    base_filters = (
        filters.incoming & filters.text & filters.command(command, ["/", Config.COMMAND_HANLDER_BOT])
    )

    def decorator(func):
        async def wrapper(client: Client, message: Message):
            _debug(f"Called {func.__name__}")

            try:
                await message.initialise_attributes()
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
                    _exception(
                        f"Module: {func.__module__} - Function: {func.__name__}: {e1}"
                    )
                except BaseException as e2:
                    _error("An exception occured while handling of another exception: ")

                    _exception(
                        f"Module: {func.__module__} - Function: {func.__name__}: {e2} during {e1}"
                    )

        add_bot_handler(base_filters, wrapper, func.__name__)
        return wrapper
    return decorator