#from Main import ClientData
#
#from Main.core.decorators import app
#from Main.core.types import Client, Message
#
#@app.on_command(
#    "help",
#    {
#        "help": "retrieves help about a command/module/function",
#        "example": "help"
#    },
#    {
#        "args": {
#            
#            "m": {
#                "usage": "get module info (default behaviour)",
#                "example": "help -m <module name>",
#            },
#            "c": {
#                "usage": "get command info",
#                "example": "help -c <command name>",
#            },
#            "f": {
#                "usage": "get function info",
#                "example": "help -f <function name>",
#            },
#        }
#    },
#    False,
#    requires_input_if_arguments = True
#)
#async def help(client: Client, message: Message):
#    print(1)
#    if message.args:
#        print(2, message.args)
#        match message.args[0]:
#            case "m":
#                if module_info := ClientData.app_help_menu.get(message.input):
#                    # result: list[str] = []
#                    # for num, command in enumerate(module_info):
#                    #     result.append(
#                    #         f"{num + 1}. {command[0]}:" +
#                    #         f"Aliases: {command[1]['aliases']}" if command[1]
#                    #     )
#                    # 
#
#                    result: list[str] = [f"Module name: {message.input}"]
#
#                    for num, command in enumerate(module_info):
#                        result.append(
#                            f"{num + 1}. {command[0]}" +
#                            ((f"Aliases: " + ", ".join(x)) if (x := command[1]['aliases']) else "") + "\n"
#                            f"Help: {(help := command[1]['command_help'])['help']}\n" +
#                            f"Example: {help['example']}\n" +
#                            f"todo"
#                        )
#                    
#                    return await message.edit("\n".join(result))
#
#                
#                return message.edit(f"Module `{message.input}` not found.")
#
#            case "c":
#                await message.edit("todo c")
#
#            case "f":
#                await message.edit("todo f")
#    
#            case _:
#                pass
#    
#    
#
#    #if module_info := ClientData.app_help_menu.get(message.input):
#    #    print(message.args)
#    #    match message.args:
#    #        case "m":
#    #            format: list[str] = []
#    #            for num, command_info in enumerate(module_info):
#    #                format.append(
#    #                    f"{num+1}. {command_info[0]}: {command_info[1]}"
#    #                )
#    #
#    #                await message.edit("\n".join(format))
#    #                
#    #        case _:
#    #            await message.edit("todo")