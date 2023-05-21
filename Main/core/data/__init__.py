#from typing import Any, Union
#
#class ClientData_Definitions:
#    admin_only = slice(0, 0)
#    group_only = slice(0, 1)
#    channel_only = slice(0, 2)
#    private_only = slice(0, 3)
#
#    requires_input = slice(1, 0)
#    requires_reply = slice(1, 1)
#
#class ClientData:
#    """
#    `app_help_menu|bot_help_menu`: Is a list of dictionaries which has the `plugin_file_name` as their key,
#    the given dictionary has ... todo
#    """
#    data: dict[str, Any] = {}
#    app_commands: list[str] = []
#    bot_commands: list[tuple[str, list[str]]] = []
#    app_help_menu: dict[str, list[tuple[str, dict[str, Any]]]] = {}
#    bot_help_menu: dict[str, list[tuple[str, dict[str, Any]]]] = {}
#        
#    """
#    {
#        module_name: [
#            (
#                command: str,
#                {
#                    aliases: [],
#                    command_help: {
#                        "help": str,
#                        "example": str
#                    },
#
#                    arguments: {
#                        "args": { # none
#                            ""
#                        }
#
#                        "kwargs"
#                    }
#
#                    multiple,
#                    admin/gc/ch/pv only + rq input/reply
#                }
#            )
#        ]
#    }
#    
#    """
#
#    #def get_attr(self, key: str) -> Any:
#    #    return self.__getattribute__(key)
##
#    #def set_attr(self, key: str, value: Any) -> None:
#    #    self.__setattr__(key, value)
##
#    #def get_data(self, key: str) -> Any:
#    #    return self.data.get(key)
##
#    #def set_data(self, key: str, value: Any) -> None:
#    #    self.data[key] = value