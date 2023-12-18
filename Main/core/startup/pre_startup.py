from os import path, mkdir

from Main import Config
from Main.core.types import Client
from Main.core.helpers.logging_helper import (
        info as _info, error as _error, warn as _warn, exception as _exception, empty as _empty
    )

def load_clients() -> tuple[list[Client], list[Client]]:
    clients: tuple[list[Client], list[Client]] = ([], [])
    _empty()

    for num, name in enumerate(["app", "bot"]):
        session_strings_or_bot_tokens: list[str] = (
            Config.ALL_BOT_TOKENS if num else Config.ALL_SESSION_STRINGS
        )

        length: int = len(session_strings_or_bot_tokens)

        for index, string_or_token in enumerate(session_strings_or_bot_tokens):
            try:
                clients[num].append(
                    Client(
                        f"{index}@{name}", Config.API_ID, Config.API_HASH, # type: ignore
                        bot_token = string_or_token if num else None,  # type: ignore
                        session_string = None if num else string_or_token  # type: ignore
                    )
                )

                _info(f"Loaded [{name.upper()}]: {index + 1}/{length}")

            except BaseException as e:
                _exception(str(e))

                if index:
                    _error(f"Couldn't load [{name.upper()}]: {num + 1}/{length}")
                else:
                    _error(f"Couldn't load main [{name.upper()}]. Exitting...")
                    quit()

        _empty()

    return clients

def configure_directories():
    for directory in ["Logs"] + Config.CUSTOM_DIRECTORIES:
        if not path.exists(directory):
            mkdir(directory)

    _info("Directory configuration completed.")