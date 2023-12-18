from Main.core.helpers.regex_helper import Compiled as _Compiled

class MessageHelper:
    @staticmethod
    def process_input(text: str) -> tuple[str, list[str], dict[str, str], str]:
        if match := _Compiled.command_match.match(text):
            raw_match = match.group()
            input = text[len(match.group()):]
            cmd, arguments = raw_match[1:].split(" ", 1)
            args = [i for i in _Compiled.command_match_args.findall(arguments)]
            kwargs = {i[0]: i[1] for i in _Compiled.compile_match_kwargs.findall(arguments)}
        else:
            cmd, input = (text[1:] + " ").split(" ", 1)
            args, kwargs = [], {}

        return input, args, kwargs, cmd