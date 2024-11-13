from typing import Optional, cast
from logging import NOTSET, INFO, DEBUG
from dotenv import load_dotenv as _load_dotenv

from Main.core.helpers.regex_helper import str_to_dict
from Main.core.helpers.misc_helper import set_as_empty
from Main.core.helpers import env_helper as _env_helper


_load_dotenv()

get_env = _env_helper.get_env_or_default
get_env_int = _env_helper.get_env_int_or_None
get_env_bool = _env_helper.get_env_bool_or_default

# regex = re.compile(r"\([a-zA-Z_]\w*\s*,\s*.*?\),*")

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

    API_ID: int = cast(int, get_env_int("API_ID"))
    API_HASH: str = cast(str, get_env("API_HASH"))

    OWNER_ID: int = cast(int, get_env_int("OWNER_ID", True))

    MAIN_SESSION: Optional[str] = get_env("MAIN_SESSION")

    COMMAND_HANDLER_APP: str = cast(str, get_env("COMMAND_HANDLER_APP", False, "."))
    COMMAND_HANDLER_BOT: str = cast(str, get_env("COMMAND_HANDLER_BOT", False, "!"))

    TIME_ZONE: Optional[str] = get_env("TIME_ZONE", False, "Asia/Kolkata")

    DB_CHAT_ID: int = cast(int, get_env_int("DB_CHAT_ID"))
    LOG_CHAT_ID: Optional[int] = get_env_int("LOG_CHAT_ID", False)
    START_UP_CHAT_ID: Optional[int] = get_env_int("START_UP_CHAT_ID", False)
    PLUGIN_CHANNEL_CHAT_ID: Optional[int] = get_env_int("PLUGIN_CHANNEL_CHAT_ID", False)

    START_UP_TEXT: str = cast(str, get_env("START_UP_TEXT", False, "Bot has started!"))

    SUDO_USERS: list[int] = [int(i) for i in cast(str, get_env("SUDO_USERS", False, "")).split(' ') if i.isdigit()]
    DISABLE_SUDO_USERS: bool = get_env_bool("DISABLE_SUDO_USERS", False, False)

    INFO_UPDATE_TIME_SEC: int | None = get_env_int("INFO_UPDATE_TIME_SEC", False)

    _SESSION_STRINGS: list[str] = cast(str, get_env("SESSION_STRINGS", False, "")).split(' ')
    _BOT_TOKENS: list[str] = cast(str, get_env("BOT_TOKENS", False, "")).split(' ')

    _MAIN_MODULE_PLUGIN_NO_LOAD_APP: list[str] = cast(str, get_env("MAIN_MODULE_PLUGIN_NO_LOAD_APP", False, "")).split(' ')
    _MAIN_MODULE_PLUGIN_NO_LOAD_BOT: list[str] = cast(str, get_env("MAIN_MODULE_PLUGIN_NO_LOAD_APP", False, "")).split(' ')

    _MODULE_PLUGIN_NO_LOAD_APP: list[str] = cast(str, get_env("MODULE_PLUGIN_NO_LOAD_APP", False, "")).split(' ')
    _MODULE_PLUGIN_NO_LOAD_BOT: list[str] = cast(str, get_env("MODULE_PLUGIN_NO_LOAD_BOT", False, "")).split(' ')

    _MAIN_FUNC_PLUGIN_NO_LOAD_APP: list[str] = cast(str, get_env("MAIN_FUNC_PLUGIN_NO_LOAD_APP", False, "")).split(' ')
    _MAIN_FUNC_PLUGIN_NO_LOAD_BOT: list[str] = cast(str, get_env("MAIN_FUNC_PLUGIN_NO_LOAD_BOT", False, "")).split(' ')

    _FUNC_PLUGIN_NO_LOAD_APP: list[str] = cast(str, get_env("FUNC_PLUGIN_NO_LOAD_APP", False, "")).split(' ')
    _FUNC_PLUGIN_NO_LOAD_BOT: list[str] = cast(str, get_env("FUNC_PLUGIN_NO_LOAD_BOT", False, "")).split(' ')

    # For developers

    DEBUG: bool = get_env_bool("DEBUG", False)
    SUPER_LOG: bool = get_env_bool("DEBUG", True)
    SUPER_LOG_LEVEL: int = _get_log_level() if SUPER_LOG else NOTSET
    SUPER_LOG_TO_CONSOLE: bool = get_env_bool("SUPER_LOG_TO_CONSOLE", False, False)

    FORCE: bool = get_env_bool("FORCE", False)

    CUSTOM_CONFIGS_FORMAT: int = get_env_int("CUSTOM_CONFIGS_FORMAT", False) or 1

    _CUSTOM_DIRECTORIES: list[str] = cast(str, get_env("CUSTOM_DIRECTORIES", False, "")).split(' ')
    CUSTOM_CONFIGS: dict[str, str] = str_to_dict(cast(str, get_env("CUSTOM_CONFIGS", False, "")), CUSTOM_CONFIGS_FORMAT)

    FAST_LOAD: bool = get_env_bool("FAST_LOAD", False, True)

    # Conditional Statements and Fallbacks

    SESSION_STRINGS = cast(list[str], set_as_empty(_SESSION_STRINGS))
    BOT_TOKENS = cast(list[str], set_as_empty(_BOT_TOKENS))

    MAIN_MODULE_PLUGIN_NO_LOAD_APP = cast(list[str], set_as_empty(_MAIN_MODULE_PLUGIN_NO_LOAD_APP))
    MAIN_MODULE_PLUGIN_NO_LOAD_BOT = cast(list[str], set_as_empty(_MAIN_MODULE_PLUGIN_NO_LOAD_BOT))
    MODULE_PLUGIN_NO_LOAD_APP = cast(list[str], set_as_empty(_MODULE_PLUGIN_NO_LOAD_APP))
    MODULE_PLUGIN_NO_LOAD_BOT = cast(list[str], set_as_empty(_MODULE_PLUGIN_NO_LOAD_BOT))
    MAIN_FUNC_PLUGIN_NO_LOAD_APP = cast(list[str], set_as_empty(_MAIN_FUNC_PLUGIN_NO_LOAD_APP))
    MAIN_FUNC_PLUGIN_NO_LOAD_BOT = cast(list[str], set_as_empty(_MAIN_FUNC_PLUGIN_NO_LOAD_BOT))
    FUNC_PLUGIN_NO_LOAD_APP = cast(list[str], set_as_empty(_FUNC_PLUGIN_NO_LOAD_APP))
    FUNC_PLUGIN_NO_LOAD_BOT = cast(list[str], set_as_empty(_FUNC_PLUGIN_NO_LOAD_BOT))

    CUSTOM_DIRECTORIES = cast(list[str], set_as_empty(_CUSTOM_DIRECTORIES))

    # Compounds:

    ALL_SESSION_STRINGS: list[str] = set_as_empty([MAIN_SESSION]) + SESSION_STRINGS
    ALL_BOT_TOKENS: list[str] = set_as_empty([MAIN_BOT_TOKEN]) + BOT_TOKENS

    ALL_MODULE_PLUGIN_NO_LOAD_APP = MAIN_MODULE_PLUGIN_NO_LOAD_APP + MODULE_PLUGIN_NO_LOAD_APP
    ALL_MODULE_PLUGIN_NO_LOAD_BOT = MAIN_MODULE_PLUGIN_NO_LOAD_BOT + MODULE_PLUGIN_NO_LOAD_BOT

    ALL_FUNC_PLUGIN_NO_LOAD_APP = MAIN_FUNC_PLUGIN_NO_LOAD_APP + FUNC_PLUGIN_NO_LOAD_APP
    ALL_FUNC_PLUGIN_NO_LOAD_BOT = MAIN_FUNC_PLUGIN_NO_LOAD_BOT + FUNC_PLUGIN_NO_LOAD_BOT

    # Post Start-Up Variables:

    # Testing purposes:

    TEST: str = "?"