#from typing import Any
#
#from Main import ClientData
#
#def construct_menu(
#        command: list[str], command_help: dict[str, str],
#        arguments: dict[str, dict[str, dict[str, str]]]|None, allow_multiple_args: bool|None,
#        admin_only: bool, group_only: bool, channel_only: bool, private_only: bool,
#        requires_input: bool, requires_reply: bool, requires_arguments: bool,
#        requires_input_if_arguments: bool, reqires_reply_if_arguments: bool
#    ):
#    
#        return (
#            command[0],
#
#            {
#                "aliases": command[1:],
#                "command_help": command_help,
#                "args": arguments.get("args") if arguments else None,
#                "kwargs": arguments.get("kwarhs") if arguments else None,
#                "multiple_arguments": allow_multiple_args,
#                "requirements": (
#                    (
#                        admin_only, group_only, channel_only, private_only
#                    ),
#                    (
#                        requires_input, requires_reply, requires_arguments, requires_input_if_arguments, reqires_reply_if_arguments
#                    )
#                )
#            }
#        )
#
#def add_to_app_help_menu(
#        command: list[str],
#        command_help: dict[str, str],
#
#        arguments: dict[str, dict[str, dict[str, str]]]|None,
#        allow_multiple_args: bool|None,
#
#        admin_only: bool,
#        group_only: bool,
#        channel_only: bool,
#        private_only: bool,
#
#        requires_input: bool,
#        requires_reply: bool,
#        requires_arguments: bool,
#        requires_input_if_arguments: bool,
#        requires_reply_if_arguments: bool,
#
#        plugin_file_name: str,
#    ):
#        plugin_file_name = plugin_file_name.split(".")[-1:][0]
#        new_menu = construct_menu(
#                command, command_help,
#                arguments, allow_multiple_args,
#                admin_only, group_only, channel_only, private_only,
#                requires_input, requires_reply, requires_arguments, requires_input_if_arguments, requires_reply_if_arguments
#            )
#
#        if (menu := ClientData.app_help_menu.get(plugin_file_name)): # type: ignore
#               menu.append(new_menu)
#               ClientData.app_commands.append(plugin_file_name)
#        else:
#            ClientData.app_help_menu[plugin_file_name] = [new_menu]