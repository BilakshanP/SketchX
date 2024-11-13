from time import sleep
from typing import Any, Callable, Coroutine, Awaitable

from pyrogram import filters, StopPropagation, ContinuePropagation

from pyrogram.types import ReplyKeyboardMarkup

from Main import Config, Menu
from Main.core.types import Client, Message
from Main.core.types.module import Arg, KwArg, Arguments, Command, Help
from Main.core.helpers.decorator_helper import process_bot_message
from Main.core.helpers.handler_helper import add_bot_handler 
from Main.core.helpers.logging_helper import error as _error, exception as _exception, debug as _debug 


def on_command(
        command: str | list[str],
        help: str,
        example: str,

        args: list[Arg] = [],
        kwargs: list[KwArg] = [],

        multiple_args: bool = False,

        sudo_only: bool = True,

        admin_only: bool = False,
        group_only: bool = False,
        channel_only: bool = False,
        private_only: bool = False,

        requires_input: bool = False,
        requires_reply: bool = False,

        requires_arguments: bool = False,
        requires_reply_if_arguments: bool = False,
        requires_input_if_arguments: bool = False,

        requires_keyword_arguments: bool = False,
        requires_reply_if_keyword_arguments: bool = False,
        requires_input_if_keyword_arguments: bool = False,

        delete: bool = False,
        delete_delay: float = 2.5,

        deny_if_sender_is_channel: bool = False,

        group: int = 1,

        module_author: str = '',
        module_author_remarks: str = ''
) -> Callable[[Client, Message], Coroutine[Any, Any, Message | None]]:
    if isinstance(command, str):
        command = [command]

    base_filters = (
        filters.incoming & filters.text & filters.command(command, ["/", Config.COMMAND_HANDLER_BOT])
    )

    def decorator(func: Callable[[Client, Message], Awaitable[Message | list[Message] | None]]): 
        async def wrapper(client: Client, message: Message): 
            _debug(f"Called {func.__module__}.{func.__name__}")

            await message.initialise_attributes()

            cmd: str = f"`{Config.COMMAND_HANDLER_BOT}{message.cmd}`"

            processed_message = await Message.from_raw_message_or_none(
                await process_bot_message(
                    client, message, cmd, multiple_args,
                    sudo_only, admin_only, group_only, channel_only, private_only,
                    requires_input, requires_reply,
                    requires_arguments, requires_input_if_arguments, requires_reply_if_arguments,
                    requires_keyword_arguments, requires_input_if_keyword_arguments, requires_reply_if_keyword_arguments,
                    deny_if_sender_is_channel
                )
            )

            if processed_message is not None:
                return processed_message

            try:
                result: Message | list[Message] | None = await func(client, message) 

                if delete and result is not None:
                    sleep(delete_delay)

                    if isinstance(result, Message):
                        result = [result]

                    for i in result: 
                        try:
                            await i.delete() 
                        except Exception as e:
                            _error(f"Couldn't delete message after execution.")

                            _exception(f"Module: {func.__module__} - Function: {func.__name__}: {e}")

            except StopPropagation:
                raise StopPropagation
            except ContinuePropagation:
                raise ContinuePropagation
            except Exception as e1:
                try:
                    await message.reply_text("Something went wrong, check logs.") 
                    _exception(
                        f"Module: {func.__module__} - Function: {func.__name__}: {e1}"
                    )
                except Exception as e2:
                    _error("An exception occured while handling of another exception: ")
                    _exception(
                        f"Module: {func.__module__} - Function: {func.__name__}: {e2} during {e1}"
                    )

        add_bot_handler(wrapper, base_filters, func.__name__, group)
        Menu.add_bot_command(
            Command(
                command, Help(help, example), Arguments(args, kwargs), multiple_args,
                admin_only, group_only, channel_only, private_only,
                requires_input, requires_reply,
                requires_arguments, requires_input_if_arguments, requires_reply_if_arguments,
                requires_keyword_arguments, requires_reply_if_keyword_arguments, requires_input_if_keyword_arguments,
                delete, delete_delay, deny_if_sender_is_channel,
                module_author if module_author else "@Redditard", module_author_remarks
            ),
            func.__module__.split(".")[-1], func.__name__,
        )
        return wrapper
    return decorator