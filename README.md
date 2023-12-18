<h1 align="center">
    <b>
        >_ | SketchX
    </b>
</h1>

Credits: Altruix/Altruix, TheHamkerCat/WilliamButcherBot & DevsExpo/Friday

``` python
def on_command(
        command: Union[str, list[str]] = ["example"],
        command_help: dict[str, str] = {
            "help": "This is an example help.",
            "example": f"{Config.COMMAND_HANDLER_APP}example"
        },

        arguments: dict[str, dict[str, dict[str, str]]]|None = {
            "args": {
                "a": {
                    "usage": "It's an example argument, and can only be 1 character wide.",
                    "example": ".example -a <text/reply here>"
                },

                "b": {
                    "usage": "It's an example argument, and multiple can be passed together.",
                    "example": ".example -a -b <text/reply here>"
                }
            },

            "kwargs": {
                "arg1": {
                    "usage": "It's an example keyword-argument, and can only be more that 1 character wide.",
                    "example": ".example --arg1=value <text/reply here>"
                },
                "arg2": {
                    "usage": "It's an example keyword-argument, and can be used with a simple argument too.",
                    "example": ".example -a --arg2=100 --arg1=99 -b <text/reply here>"
                }
            }
        },

        allow_multiple_args: bool|None = True,

        admin_only: bool = False,
        group_only: bool = False,
        channel_only: bool = False,
        private_only: bool = False,

        requires_input: bool = False,
        requires_reply: bool = False,
):
    pass
```
<!--

For any help regarding Markdown:
    https://github.com/Kernix13/markdown-cheatsheet
    https://github.com/tchapi/markdown-cheatsheet
    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

    https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams

    https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf

-->