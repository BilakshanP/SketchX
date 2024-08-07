import re

from typing import Optional
from logging import NOTSET, INFO, DEBUG

from Main.core.helpers.regex_helper import str_to_dict
from Main.core.helpers.misc_helper import set_to_empty
from Main.core.helpers import env_helper as _env_helper

_env_helper._load_dotenv() # type: ignore

get_env = _env_helper.get_env_or_default
get_env_int = _env_helper.get_env_int_or_None
get_env_bool = _env_helper.get_env_bool_or_default

regex = re.compile(r"\([a-zA-Z_]\w*\s*,\s*.*?\),*")


def _get_log_level() -> int:
    match get_env("SUPER_LOG_LEVEL", False):
        case "INFO": return INFO
        case "DEBUG": return DEBUG
        case _: return NOTSET



class Config:
    """
    Configuartion variables of bot:
        todo
    """

    IS_LOCAL_DEPLOY: bool = get_env_bool("IS_LOCAL_DEPLOY", False)

    MAIN_BOT_TOKEN: Optional[str] = get_env("MAIN_BOT_TOKEN")

    ALIVE_IMAGE: Optional[str] = get_env("ALIVE_IMAGE", False, "https://telegra.ph//file/bdacc5cdac69ea353190c.png")
    START_IMAGE: Optional[str] = get_env("START_IMAGE", False, "https://telegra.ph//file/bdacc5cdac69ea353190c.png")

    API_ID: Optional[int] = get_env_int("API_ID")
    API_HASH: Optional[str] = get_env("API_HASH")

    OWNER_ID: int = get_env_int("OWNER_ID", True) # type: ignore

    MAIN_SESSION: Optional[str] = get_env("MAIN_SESSION") 

    COMMAND_HANDLER_APP: str = get_env("COMMAND_HANDLER_APP", False, ".") # type: ignore
    COMMAND_HANDLER_BOT: str = get_env("COMMAND_HANDLER_BOT", False, "!") # type: ignore

    TIME_ZONE: Optional[str] = get_env("TIME_ZONE", False, "Asia/Kolkata")

    DB_CHAT_ID: int = get_env_int("DB_CHAT_ID") # type: ignore
    LOG_CHAT_ID: Optional[int] = get_env_int("LOG_CHAT_ID", False)
    START_UP_CHAT_ID: Optional[int] = get_env_int("START_UP_CHAT_ID", False)
    PLUGIN_CHANNEL_CHAT_ID: Optional[int] = get_env_int("PLUGIN_CHANNEL_CHAT_ID", False)

    START_UP_TEXT: str = get_env("START_UP_TEXT", False, "Bot has started!") # type: ignore

    SESSION_STRINGS: list[str] = get_env("SESSION_STRINGS", False, "").split(' ') # type: ignore
    BOT_TOKENS: list[str] = get_env("BOT_TOKENS", False, "").split(' ') # type: ignore

    SUDO_USERS: list[int] = [int(i) for i in get_env("SUDO_USERS", False, "").split(' ') if i.isdigit()] # type: ignore
    DISABLE_SUDO_USERS: bool = get_env_bool("DISABLE_SUDO_USERS", False, False)

    MAIN_MODULE_PLUGIN_NO_LOAD_APP: list[str] = get_env("MAIN_MODULE_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MAIN_MODULE_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MAIN_MODULE_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore

    MODULE_PLUGIN_NO_LOAD_APP: list[str] = get_env("MODULE_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MODULE_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MODULE_PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    MAIN_FUNC_PLUGIN_NO_LOAD_APP: list[str] = get_env("MAIN_FUNC_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MAIN_FUNC_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MAIN_FUNC_PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    FUNC_PLUGIN_NO_LOAD_APP: list[str] = get_env("FUNC_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    FUNC_PLUGIN_NO_LOAD_BOT: list[str] = get_env("FUNC_PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    # For developers

    DEBUG: bool = get_env_bool("DEBUG", False)
    SUPER_LOG: bool = get_env_bool("DEBUG", True)
    SUPER_LOG_LEVEL: int = _get_log_level() if SUPER_LOG else NOTSET
    SUPER_LOG_TO_CONSOLE: bool = get_env_bool("SUPER_LOG_TO_CONSOLE", False, False)

    FORCE: bool = get_env_bool("FORCE", False)

    CUSTOM_CONFIGS_FORMAT: int = get_env_int("CUSTOM_CONFIGS_FORMAT", False) or 1

    CUSTOM_DIRECTORIES: list[str] = get_env("CUSTOM_DIRECTORIES", False, "").split(' ') # type: ignore
    CUSTOM_CONFIGS: dict[str, str] = str_to_dict(
                                            get_env("CUSTOM_CONFIGS", False, ""), # type: ignore
                                            CUSTOM_CONFIGS_FORMAT
                                        )

    FAST_LOAD: bool = get_env_bool("FAST_LOAD", False, True)

    # Conditional Statements and Fallbacks

    SESSION_STRINGS = set_to_empty(SESSION_STRINGS) # type: ignore
    BOT_TOKENS = set_to_empty(BOT_TOKENS) # type: ignore

    MAIN_MODULE_PLUGIN_NO_LOAD_APP = set_to_empty(MAIN_MODULE_PLUGIN_NO_LOAD_APP) # type: ignore
    MAIN_MODULE_PLUGIN_NO_LOAD_BOT = set_to_empty(MAIN_MODULE_PLUGIN_NO_LOAD_BOT) # type: ignore
    MODULE_PLUGIN_NO_LOAD_APP = set_to_empty(MODULE_PLUGIN_NO_LOAD_APP) # type: ignore
    MODULE_PLUGIN_NO_LOAD_BOT = set_to_empty(MODULE_PLUGIN_NO_LOAD_BOT) # type: ignore
    MAIN_FUNC_PLUGIN_NO_LOAD_APP = set_to_empty(MAIN_FUNC_PLUGIN_NO_LOAD_APP) # type: ignore
    MAIN_FUNC_PLUGIN_NO_LOAD_BOT = set_to_empty(MAIN_FUNC_PLUGIN_NO_LOAD_BOT) # type: ignore
    FUNC_PLUGIN_NO_LOAD_APP = set_to_empty(FUNC_PLUGIN_NO_LOAD_APP) # type: ignore
    FUNC_PLUGIN_NO_LOAD_BOT = set_to_empty(FUNC_PLUGIN_NO_LOAD_BOT) # type: ignore

    CUSTOM_DIRECTORIES = set_to_empty(CUSTOM_DIRECTORIES) # type: ignore

    # Compounds:

    ALL_SESSION_STRINGS: list[str] = [MAIN_SESSION] + SESSION_STRINGS # type: ignore
    ALL_BOT_TOKENS: list[str] = [MAIN_BOT_TOKEN] + BOT_TOKENS # type: ignore

    ALL_MODULE_PLUGIN_NO_LOAD_APP = MAIN_MODULE_PLUGIN_NO_LOAD_APP + MODULE_PLUGIN_NO_LOAD_APP
    ALL_MODULE_PLUGIN_NO_LOAD_BOT = MAIN_MODULE_PLUGIN_NO_LOAD_BOT + MODULE_PLUGIN_NO_LOAD_BOT

    ALL_FUNC_PLUGIN_NO_LOAD_APP = MAIN_FUNC_PLUGIN_NO_LOAD_APP + FUNC_PLUGIN_NO_LOAD_APP
    ALL_FUNC_PLUGIN_NO_LOAD_BOT = MAIN_FUNC_PLUGIN_NO_LOAD_BOT + FUNC_PLUGIN_NO_LOAD_BOT

    # Post Start-Up Variables:

    # Testing purposes:

    TEST: str = "?"