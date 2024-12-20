from time import sleep

from pyrogram import filters, StopPropagation, ContinuePropagation

from Main import Config, Menu
from Main.core.filters import sudo_filter
from Main.core.types import Client, Message, MessageOrNone, HandlerDecoratorType, AsyncPlugin
from Main.core.types.module import Arg, KwArg, Arguments, Command, Help
from Main.core.helpers.decorator_helper import process_app_message
from Main.core.helpers.misc_helper import is_present
from Main.core.helpers.handler_helper import add_app_handler 
#from Main.core.helpers.module_helpers.help_menu_helper import add_to_app_help_menu
from Main.core.helpers.logging_helper import (
        error as _error, warn as _warn, exception as _exception, debug as _debug
    )


def on_command( 
        command: str | list[str],
        help: str,
        example: str,

        args: list[Arg] = [],
        kwargs: list[KwArg] = [],

        multiple_args: bool = False,

        sudo_only: bool = False,
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
# ) -> Callable[[Client, Message], Coroutine[Any, Any, Message | None]]:
) -> HandlerDecoratorType:
    if isinstance(command, str):
        command = [command]

    base_filters = (
        (filters.me | sudo_filter)
        & filters.command(command, Config.COMMAND_HANDLER_APP)
        & ~ (filters.via_bot | filters.forwarded)
    )

    def decorator(func: AsyncPlugin) -> AsyncPlugin: 
        async def wrapper(client: Client, message: Message) -> MessageOrNone:
            _debug(f"Called {func.__module__}.{func.__name__}")


            if Config.FORCE or not is_present("#NoUB", [message.chat.title, message.chat.first_name, message.chat.last_name]):
                # await message.initialise_attributes()
                message = await Message.from_raw_message(message)

                _debug(f"Raw text: {message.text}, Command: {message.cmd}, Input: {message.input}, Args: {message.args}, Kwargs: {message.kwargs}, Chat Type: {message.chat_type}")

                cmd: str = f"`{Config.COMMAND_HANDLER_APP}{message.cmd}`"

                processed_message = await Message.from_raw_message_or_none(
                    await process_app_message(
                        client, message, cmd, multiple_args,
                        sudo_only, admin_only, group_only, channel_only, private_only,
                        requires_input, requires_reply,
                        requires_arguments, requires_input_if_arguments, requires_reply_if_arguments,
                        requires_keyword_arguments, requires_input_if_keyword_arguments,requires_reply_if_keyword_arguments,
                        deny_if_sender_is_channel
                    )
                )

                if processed_message is not None:
                    return processed_message

                try:
                    result = await func(client, message) 

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
                        await message.edit("Something went wrong, check logs.")
                        _exception(
                            f"Module: {func.__module__} - Function: {func.__name__}: {e1}"
                        )
                    except Exception as e2:
                        _error("An exception occured while handling of another exception: ")

                        _exception(
                            f"Module: {func.__module__} - Function: {func.__name__}: {e2} during {e1}"
                        )

            else:
                _warn(f"Can't fulfill this request, as the [chat](https://t.me/c/{message.chat.id}/{message.id}) contains \"#NoUB\" in its title and doesn't allow the use of userbots.")

        add_app_handler(wrapper, base_filters, func.__name__, group)

        Menu.add_app_command(
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

        #add_to_app_help_menu(command, command_help, arguments, allow_multiple_args, admin_only, group_only, channel_only, private_only, requires_input, requires_reply, requires_arguments, requires_input_if_arguments, requires_input_if_arguments, func.__module__)
        return wrapper
    return decorator 