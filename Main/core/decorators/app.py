from time import sleep
from typing import Union, Callable

from pyrogram import filters, StopPropagation, ContinuePropagation

from Main import Config, Menu
from Main.core.filters import sudo_filter
from Main.core.types import Client, Message
from Main.core.types.module import Arg, Kwarg, Argument, Command, Help
from Main.core.helpers.misc_helper import is_present
from Main.core.helpers.handler_helper import add_app_handler # type: ignore
#from Main.core.helpers.module_helpers.help_menu_helper import add_to_app_help_menu
from Main.core.helpers.logging_helper import (
        error as _error, warn as _warn, exception as _exception, debug as _debug
    )


def on_command( # type: ignore
        command: Union[str, list[str]],
        help: str,
        example: str,

        args: list[Arg] = [],
        kwargs: list[Kwarg] = [],

        multiple_args: bool = False,

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

        module_author: str|None = None,
        module_author_remarks: str|None = None
):
    if isinstance(command, str):
        command = [command]

    base_filters = (
        (filters.me | sudo_filter)
        & filters.command(command, Config.COMMAND_HANDLER_APP)
        & ~ (filters.via_bot | filters.forwarded)
    )

    def decorator(func: Callable): # type: ignore
        async def wrapper(client: Client, message: Message):
            _debug(f"Called {func.__module__}.{func.__name__}")

            if Config.FORCE or not is_present("#NoUB", [message.chat.title, message.chat.first_name, message.chat.last_name]):
                await message.initialise_attributes()

                cmd: str = f"`{Config.COMMAND_HANDLER_APP}{message.cmd}`"

                if deny_if_sender_is_channel and (rtm := message.reply_to_message) and (sc := rtm.sender_chat) and sc.id:
                    return await message.edit(f"A channel can't execute {cmd} command.")

                # if admin_only...

                if group_only and message.chat_type not in "supergroup":
                    return await message.edit(f"Command {cmd} can only be used in a group chat.")
                if channel_only and message.chat_type != "channel":
                    return await message.edit(f"Command {cmd} can only be used in a channel.")
                if private_only and message.chat_type != "private":
                    return await message.edit(f"Command {cmd} can only be used in a private chat.")
                if requires_input and message.input == '':
                    return await message.edit(f"An input is required to execute {cmd} command.")
                if requires_reply and not message.reply_to_message:
                    return await message.edit(f"A reply is required to execute {cmd} command.")
                if requires_arguments and not message.args:
                    return await message.edit(f"An argument is required to execute {cmd} command.")
                if requires_keyword_arguments and not message.kwargs:
                    return await message.edit(f"A keyword argument is required to execute {cmd} command.")
                if message.args:
                    if requires_input_if_arguments and not message.input:
                        return await message.edit(f"An input is required if arguments are passed to {cmd} command.")
                    if requires_reply_if_arguments and not message.reply_to_message:
                        return await message.edit(f"A reply is required if arguments are passed to {cmd} command.")
                if message.kwargs:
                    if requires_input_if_keyword_arguments and not message.input:
                        return await message.edit(f"An input is required if keyword arguments are passed to {cmd} command.")
                    if requires_reply_if_keyword_arguments and not message.reply_to_message:
                        return await message.edit(f"A reply is required if keyword arguments are passed to {cmd} command.")
                if not multiple_args and len(message.args) > 1:
                    return await message.edit(f"Command {cmd} doesn't allow multiple arguments.")

                try:
                    result: Union[Message, list[Message]] = await func(client, message) # type: ignore

                    if delete:
                        sleep(delete_delay)

                        if isinstance(result, Message):
                            result = [result]

                        for i in result: # type: ignore
                            try:
                                i.delete() # type: ignore
                            except BaseException as e:
                                _error(f"Couldn't delete message after execution.")

                                _exception(f"Module: {func.__module__} - Function: {func.__name__}: {e}")

                except StopPropagation:
                    raise StopPropagation
                except ContinuePropagation:
                    raise ContinuePropagation
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

            else:
                _warn(f"Can't fulfill this request, as the [chat](https://t.me/c/{message.chat.id}/{message.id}) contains \"#NoUB\" in its title and doesn't allow the use of userbots.")

        add_app_handler(wrapper, base_filters, func.__name__, group)

        Menu.add_app_command(
            Command(
                command, Help(help, example), Argument(args, kwargs), multiple_args,
                admin_only, group_only, channel_only, private_only,
                requires_input, requires_reply,
                requires_arguments, requires_input_if_arguments, requires_reply_if_arguments,
                requires_keyword_arguments, requires_reply_if_keyword_arguments, requires_input_if_keyword_arguments,
                delete, delete_delay, deny_if_sender_is_channel,
                module_author if module_author is not None else "@Redditard", module_author_remarks
            ),
            func.__module__.split(".")[-1], func.__name__,
        )

        #add_to_app_help_menu(command, command_help, arguments, allow_multiple_args, admin_only, group_only, channel_only, private_only, requires_input, requires_reply, requires_arguments, requires_input_if_arguments, requires_input_if_arguments, func.__module__)
        return wrapper
    return decorator # type: ignore