from Main.core.data import HelpMenu
from Main.core.types import Client, Message

from Main.core.decorators import app

@app.on_command("h", "", "")
async def help_help(client: Client, message: Message):
    if menu := HelpMenu.app_help_menu.get(message.input):
        text = f"**Module**: `{menu.module_name}` by __{menu.module_author}__\n" + "\n".join(
            [
                (
                    f"{n + 1}. {menu.functions[n]}: {i.name}\n" +
                    f"Aliases: {str(aliases)[1:-1]}" if (aliases := i.aliases) else ""
                ) for n, i in enumerate(menu.commands)
            ]
        )
        
        await message.edit(text)

@app.on_command("help", "get help", "help")
async def help(client: Client, message: Message):
    if menu := HelpMenu.app_help_menu.get((input := message.input)):
        text = f"**Module**: `{menu.module_name}` by {menu.module_author}\n"
        if menu.count == 0:
            await message.edit(text + "\nContains no registered commands/functions.")
        else:
            for n, i in enumerate(menu.commands):
                text += f"{n + 1}. {i.name} in {menu.functions[n]}\n"
                if (aliases := i.aliases):
                    text += f"Aliases {str(aliases)[1:-1]}\n"
            
            await message.edit(text)
    else:
        await message.edit(f"Module `{input}` not found.")