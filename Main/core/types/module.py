from typing import Any

class Arg:
    def __init__(self, key: str, usage: str, example: str):
        self.key = key
        self.usage = usage
        self.example = example

class Kwarg:
    def __init__(self, key: str, value: Any, usage: str, example: str):
        self.key = key
        self.value = value
        self.usage = usage
        self.example = example

class Argument:
    def __init__(self, args: list[Arg], kwargs: list[Kwarg]):
        self.args = args
        self.kwargs = kwargs

class Command:
    def __init__(self, name: str, aliases: list[str], arguments: Argument,
                 multiple_args: bool = True, admin_only: bool = False,
                 group_only: bool = False, channel_only: bool = False,
                 private_only: bool = False, requires_input: bool = False,
                 requires_reply: bool = False, requires_input_if_arguments: bool = False,
                 requires_reply_if_arguments: bool = False):
        self.name = name
        self.aliases = aliases
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
    def __init__(self, module_name: str, module_type: str, module_author: str):
        self.module_name = module_name
        self.module_type = module_type
        self.module_author = module_author
        self.commands = []
    
    def add_command(self, name: str, aliases: list[str], args: Argument,
                   multiple_args: bool = True, admin_only: bool = False,
                   group_only: bool = False, channel_only: bool = False,
                   private_only: bool = False, requires_input: bool = False,
                   requires_reply: bool = False, requires_input_if_arguments: bool = False,
                   requires_reply_if_arguments: bool = False):

        command = Command(name, aliases, args, multiple_args, admin_only,
                          group_only, channel_only, private_only, requires_input,
                          requires_reply, requires_input_if_arguments, requires_reply_if_arguments)

        self.commands.append(command)