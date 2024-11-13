from pyrogram.types import Message as PyrogramMessage

from Main import Config
from Main.core.types import Client, Message

async def process_app_message(
    client: Client,
    message: Message,

    cmd: str,

    multiple_args: bool,

    sudo_only: bool,
    admin_only: bool,
    group_only: bool, 
    channel_only: bool,
    private_only: bool,

    requires_input: bool, 
    requires_reply: bool,

    requires_arguments: bool,
    requires_input_if_arguments: bool,
    requires_reply_if_arguments: bool, 

    requires_keyword_arguments: bool, 
    requires_input_if_keyword_arguments: bool,
    requires_reply_if_keyword_arguments: bool, 

    deny_if_sender_is_channel: bool
) -> PyrogramMessage | None:
    if deny_if_sender_is_channel and (rtm := message.reply_to_message) and (sc := rtm.sender_chat) and sc.id:
        return await message.edit(f"A channel can't execute {cmd} command.")
    
    # if sudo_only: ...

    if group_only and message.chat_type not in "supergroup":
        return await message.edit(f"Command {cmd} can only be used in a group chat.")
    if channel_only and message.chat_type != "channel":
        return await message.edit(f"Command {cmd} can only be used in a channel.")
    if private_only and message.chat_type != "private":
        return await message.edit(f"Command {cmd} can only be used in a private chat.")
        
    if admin_only:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        status = user.status

        if not (bool(status.ADMINISTRATOR) or bool(status.OWNER)):
            return await message.edit(f"Command {cmd} can only be used by an admin.")

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

async def process_bot_message(
    client: Client,
    message: Message,

    cmd: str,

    multiple_args: bool,

    sudo_only: bool,
    admin_only: bool,
    group_only: bool, 
    channel_only: bool,
    private_only: bool,

    requires_input: bool, 
    requires_reply: bool,

    requires_arguments: bool,
    requires_input_if_arguments: bool,
    requires_reply_if_arguments: bool, 

    requires_keyword_arguments: bool, 
    requires_input_if_keyword_arguments: bool,
    requires_reply_if_keyword_arguments: bool, 

    deny_if_sender_is_channel: bool
) -> PyrogramMessage | None:    
    if deny_if_sender_is_channel and (rtm := message.reply_to_message) and (sc := rtm.sender_chat) and sc.id:
        return await message.edit(f"A channel can't execute {cmd} command.")
    
    # if admin_only: ...


    if sudo_only and (message.from_user.id not in Config.SUDO_USERS):
        return message.reply(f"Command {cmd} can only be used by sudo users.") # type: ignore
    
    if group_only and message.chat_type not in "supergroup":
        return message.reply(f"Command {cmd} can only be used in a group chat.") # type: ignore
    
    if channel_only and message.chat_type != "channel":
        return message.reply(f"Command {cmd} can only be used in a channel.") # type: ignore
    
    if private_only and message.chat_type != "private":
        return message.reply(f"Command {cmd} can only be used in a private chat.") # type: ignore
    
    if requires_input and message.input == '':
        return message.reply(f"An input is required to execute {cmd} command.") # type: ignore
    
    if requires_reply and not message.reply_to_message:
        return message.reply(f"A reply is required to execute {cmd} command.") # type: ignore
    
    if requires_arguments and not message.args:
        return message.reply(f"An argument is required to execute {cmd} command.") # type: ignore
    
    if requires_keyword_arguments and not message.kwargs:
        return message.reply(f"A keyword argument is required to execute {cmd} command.") # type: ignore
    
    if message.args:
        if requires_input_if_arguments and not message.input:
            return message.reply(f"An input is required if arguments are passed to {cmd} command.") # type: ignore
        if requires_reply_if_arguments and not message.reply_to_message:
            return message.reply(f"A reply is required if arguments are passed to {cmd} command.") # type: ignore
    
    if message.kwargs:
        if requires_input_if_keyword_arguments and not message.input:
            return message.reply(f"An input is required if keyword arguments are passed to {cmd} command.") # type: ignore
        if requires_reply_if_keyword_arguments and not message.reply_to_message:
            return message.reply(f"A reply is required if keyword arguments are passed to {cmd} command.") # type: ignore
    
    if not multiple_args and len(message.args) > 1:
        return message.reply(f"Command {cmd} doesn't allow multiple arguments.") # type: ignore
