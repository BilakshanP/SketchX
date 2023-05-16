from Main.core.helpers.regex_helper import Compiled as _Compiled

class MessageHelper:
    @staticmethod
    def process_input(input: str): # -> tuple[str, list[str], list[str], str]:
        if match := _Compiled.command_match.match(input):
            raw_match = match.group()
            text = raw_match[len(match.group()):]
            command, arguments = raw_match[1:].split(" ", 1)
            args = [i for i in _Compiled.command_match_args.findall(arguments)]
            kwargs = {i[0]: i[1] for i in _Compiled.compile_match_kwargs.findall(arguments)}
        else:
            text, command, args, kwargs = "", input[1:], [], []

        return text, args, kwargs, command