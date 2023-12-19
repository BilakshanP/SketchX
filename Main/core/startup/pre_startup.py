import logging
from os import path, mkdir

from Main import Config
from Main.core.types import Client
from Main.core.helpers.logging_helper import info as _info, error as _error, warn as _warn, exception as _exception, empty as _empty # type: ignore


file_formatter = logging.Formatter("[%(levelname)s] @ %(asctime)s > %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
console_formatter = logging.Formatter("[X]: %(message)s")

file_handler = logging.FileHandler("logs/super.log")
file_handler.setFormatter(file_formatter)

root_logger = logging.getLogger()
root_logger.addHandler(file_handler)

if Config.SUPER_LOG_TO_CONSOLE:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)

root_logger.setLevel(Config.SUPER_LOG_LEVEL)

# Example usage
logging.info('This log message will be written to the file and printed to the console (if enabled) with the custom format')



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

            except Exception as e:
                _exception(str(e))

                if index:
                    _error(f"Couldn't load [{name.upper()}]: {num + 1}/{length}")
                else:
                    _error(f"Couldn't load main [{name.upper()}]. Exitting...")
                    quit()

        _empty()

    return clients

def configure_directories():
    for directory in Config.CUSTOM_DIRECTORIES:
        if not path.exists(directory):
            mkdir(directory)

    _info("Directory configuration completed.")