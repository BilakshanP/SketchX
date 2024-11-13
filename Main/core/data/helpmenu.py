from Main.core.types.module import Command, Module

class HelpMenu:
    app_help_menu: dict[str, Module] = {}
    bot_help_menu: dict[str, Module] = {}

    def add_app_command(self, command: Command, module_name: str, func_name: str):
        module_author = command.module_author
        module_author_remarks = command.module_author_remarks

        if menu := self.app_help_menu.get(module_name):
            pass
        else:
            menu = self.app_help_menu[module_name] = Module(module_name, module_author, module_author_remarks)

        menu.add_command(command, func_name)

    def add_bot_command(self, command: Command, module_name: str, func_name: str):
        module_author = command.module_author
        module_author_remarks = command.module_author_remarks

        if menu := self.bot_help_menu.get(module_name):
            pass
        else:
            menu = self.bot_help_menu[module_name] = Module(module_name, module_author, module_author_remarks)

        menu.add_command(command, func_name)
