from Main.core.decorators import app
from Main.core.types import Message, Client
from Main.core.types.module import KwArg

@app.on_command(
    "set",
    "Sets or changes particular parameters of the current chat.",
    "set --title=New Title",
    kwargs=[
        KwArg("tt", "<new title>", "SketchX", "Used for setting title of the chat."),
        KwArg("pic", "<reply to image>", "<reply>", "Used for setting display picture of the chat."),
        KwArg("lpic", "<image link>", "exmaple.com/pic.png", "Used for setting display picture of the chat via an image link."),
        KwArg("dsc", "<description>", "I am an exmaple description", "Used for setting description of the chat.")
    ],
    admin_only=True,
    group_only=True,
    multiple_args=False,
    requires_keyword_arguments=True
)
async def chat_setter(client: Client, message: Message):
    mk = message.kwargs
    mci = message.chat.id

    print(mk, mci)

    if (kw := mk.get("tt")):
        if message.chat.title != kw:
            if await client.set_chat_title(mci, kw):
                await message.edit("Chat title changed successfully.")
            else:
                await message.edit("Chat title couldn't be changed.")
        else:
            await message.edit("Chat title content is not modified.")

        return
    
    print(kw)

    if (kw := mk.get("pic")):
        raise NotImplementedError
    
    if (kw := mk.get("lpic")):
        if await client.set_chat_photo(mci, photo=kw):
            await message.edit("Chat photo changed successfully.")
        else:
            await message.edit("Chat photo couldn't be changed.")
        
        return
    
    if (kw := mk.get("dsc")):
        if await client.set_chat_description(mci, kw):
            await message.edit("Chat description changed successfully.")
        else:
            await message.edit("Chat description couldn't be changed.")
        
        return

    await message.edit("That's an invalid argument.")