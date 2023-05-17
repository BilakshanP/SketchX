import re

from typing import Optional

from Main.core.helpers.regex_helper import str_to_dict
from Main.core.helpers .misc_helpers import set_to_empty
from Main.core.helpers import env_helper as _env_helper, logging_helper as _logging_helper

_env_helper._load_dotenv()

get_env = _env_helper.get_env_or_default
get_env_int = _env_helper.get_env_int_or_None
get_env_bool = _env_helper.get_env_bool_or_default

regex = re.compile(r"\([a-zA-Z_]\w*\s*,\s*.*?\),*")

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

    MAIN_SESSION: Optional[str] = get_env("MAIN_SESSION") 

    COMMAND_HANDLER: str = get_env("COMMAND_HANDLER", False, ".") # type: ignore

    TIME_ZONE: Optional[str] = get_env("TIME_ZONE", False, "Asia/Kolkata")

    DB_CHAT_ID: int = get_env_int("DB_CHAT_ID") # type: ignore
    LOG_CHAT_ID: Optional[int] = get_env_int("LOG_CHAT_ID", False)
    START_UP_CHAT_ID: Optional[int] = get_env_int("START_UP_CHAT_ID", False)
    PLUGIN_CHANNEL_CHAT_ID: Optional[int] = get_env_int("PLUGIN_CHANNEL_CHAT_ID", False)

    START_UP_TEXT: str = get_env("START_UP_TEXT", False, "Bot has started!") # type: ignore

    SESSION_STRINGS: list[str] = get_env("SESSION_STRINGS", False, "").split(' ') # type: ignore
    BOT_TOKENS: list[str] = get_env("BOT_TOKENS", False, "").split(' ') # type: ignore
    
    SUDO_USERS: list[int] = [int(i) for i in get_env("SUDO_USERS", False, "").split(' ') if i.isdigit()] # type: ignore

    MAIN_PLUGIN_NO_LOAD_APP: list[str] = get_env("MAIN_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MAIN_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MAIN_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore

    PLUGIN_NO_LOAD_APP: list[str] = get_env("PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    PLUGIN_NO_LOAD_BOT: list[str] = get_env("PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    # For developers

    DEBUG: bool = get_env_bool("DEBUG", False)

    FORCE: bool = get_env_bool("FORCE", False)

    CUSTOM_CONFIGS_FORMAT: int = get_env_int("CUSTOM_CONFIGS_FORMAT", False) or 1

    CUSTOM_DIRECTORIES: list[str] = get_env("CUSTOM_DIRECTORIES", False, "").split(' ') # type: ignore
    CUSTOM_CONFIGS: dict[str, str] = str_to_dict(
                                            get_env("CUSTOM_CONFIGS", False, ""), # type: ignore
                                            CUSTOM_CONFIGS_FORMAT
                                        )

    # Conditional Statements and Fallbacks

    SESSION_STRINGS = set_to_empty(SESSION_STRINGS)
    BOT_TOKENS = set_to_empty(BOT_TOKENS)

    MAIN_PLUGIN_NO_LOAD_APP = set_to_empty(MAIN_PLUGIN_NO_LOAD_APP)
    MAIN_PLUGIN_NO_LOAD_BOT = set_to_empty(MAIN_PLUGIN_NO_LOAD_BOT)
    PLUGIN_NO_LOAD_APP = set_to_empty(PLUGIN_NO_LOAD_APP)
    PLUGIN_NO_LOAD_BOT = set_to_empty(PLUGIN_NO_LOAD_BOT)
    CUSTOM_DIRECTORIES = set_to_empty(CUSTOM_DIRECTORIES)

    ALL_PLUGIN_NO_LOAD_APP = MAIN_PLUGIN_NO_LOAD_APP + PLUGIN_NO_LOAD_APP
    ALL_PLUGIN_NO_LOAD_BOT = MAIN_PLUGIN_NO_LOAD_BOT + PLUGIN_NO_LOAD_BOT

    # Compounds:

    ALL_SESSION_STRINGS: list[str] = [MAIN_SESSION] + SESSION_STRINGS # type: ignore
    ALL_BOT_TOKENS: list[str] = [MAIN_BOT_TOKEN] + BOT_TOKENS # type: ignore

    # Post Start-Up Variables:

    # Testing purposes:

    TEST: str = "?"