from typing import Any

class Arg:
    def __init__(self, key: str, usage: str, example: str):
        self.key = key
        self.usage = usage
        self.example = example
    
    @staticmethod
    def new_from_tupled_list(tupled_list: list[tuple[str, str, str]]):
        return [Arg(i[0], i[1], i[2]) for i in tupled_list]
class Kwarg(Arg):
    pass

class Argument:
    def __init__(self, args: list[Arg], kwargs: list[Kwarg]):
        self.args = args
        self.kwargs = kwargs

class Help:
    def __init__(self, help: str, example: str):
        self.help = help
        self.example = example
class Command:
    def __init__(self, cmd: list[str], arguments: Argument, cmd_help: Help,
                 multiple_args: bool = True, admin_only: bool = False,
                 group_only: bool = False, channel_only: bool = False,
                 private_only: bool = False, requires_input: bool = False,
                 requires_reply: bool = False, requires_input_if_arguments: bool = False,
                 requires_reply_if_arguments: bool = False):
        self.cmd = cmd
        self.name = cmd[0]
        self.aliases = cmd[1:]
        self.cmd_help = cmd_help
        self.arguments = arguments
        self.multiple_args = multiple_args
        self.admin_only = admin_only
        self.group_only = group_only
        self.channel_only = channel_only
        self.private_only = private_only
        self.requires_input = requires_input
        self.requires_reply = requires_reply
        self.requires_input_if_arguments = requires_input_if_arguments
        self.requires_reply_if_arguments = requires_reply_if_arguments



class Module:
    def __init__(self, module_name: str, module_author: str):
        self.module_name = module_name
        self.module_author = module_author

        self.commands: list[Command] = []
        self.functions: list[str] = []
        self.count: int = 0
    
    def add_command(self, command: Command, func_name: str):
        self.commands.append(command)
        self.functions.append(func_name)
        self.count += 1