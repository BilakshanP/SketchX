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
    def __init__(self,
        cmd: list[str],
        cmd_help: Help,
        arguments: Argument,

        multiple_args: bool = True,

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

        module_author: str|None = None,
        module_author_remarks: str|None  = None
    ):
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

        self.requires_arguments = requires_arguments
        self.requires_input_if_arguments = requires_input_if_arguments
        self.requires_reply_if_arguments = requires_reply_if_arguments

        self.requires_keyword_arguments = requires_keyword_arguments
        self.requires_input_if_keyword_arguments = requires_input_if_keyword_arguments
        self.requires_reply_if_keyword_arguments = requires_reply_if_keyword_arguments

        self.delete = delete
        self.delete_delay = delete_delay

        self.deny_if_sender_is_channel = deny_if_sender_is_channel

        self.module_author = module_author
        self.module_author_remarks = module_author_remarks
class Module:
    def __init__(self, module_name: str, module_author: str, module_author_remarks: str|None):
        self.module_name = module_name
        self.module_author = module_author
        self.module_author_remarks = module_author_remarks

        self.commands: list[Command] = []
        self.functions: list[str] = []
        self.count: int = 0

    def add_command(self, command: Command, func_name: str):
        self.commands.append(command)
        self.functions.append(func_name)
        self.count += 1