from Main.core.types.module import Arg, Argument, Command, Module

class HelpMenu:
    app_help_menu: dict[str, Module] = {}
    bot_help_menu: dict[str, Module] = {}

    def add_app_command(self, command: Command, module_name: str, func_name: str, module_author: str):
        if menu := self.app_help_menu.get(module_name):
            pass
        else:
            menu = self.app_help_menu[module_name] = Module(module_name, module_author)
        
        menu.add_command(command, func_name)

    def add_bot_command(self, command: Command, module_name: str, func_name: str, module_author: str):
        if menu := self.bot_help_menu.get(module_name):
            pass
        else:
            menu = self.bot_help_menu[module_name] = Module(module_name, module_author)
        
        menu.add_command(command, func_name)
