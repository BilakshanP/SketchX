from .helpers import env_helper as _env_helper

_env_helper._load_dotenv()

get_env = _env_helper.get_env_or_default
get_env_int = _env_helper.get_env_int_or_None
get_env_bool = _env_helper.get_env_bool_or_default

class Config:
    """
    Configuartion variables of bot:
        todo
    """

    IS_LOCAL_DEPLOY: bool = get_env_bool("IS_LOCAL_DEPLOY", False)

    MAIN_BOT_TOKEN: str = get_env("MAIN_BOT_TOKEN") # type: ignore
    MAIN_BOT_USERNAME: str|None = get_env("MAIN_BOT_USERNAME", False) # type: ignore

    ALIVE_IMAGE: str = get_env("ALIVE_IMAGE", False, "https://telegra.ph//file/bdacc5cdac69ea353190c.png") # type: ignore
    START_IMAGE: str = get_env("START_IMAGE", False, "https://telegra.ph//file/bdacc5cdac69ea353190c.png") # type: ignore

    API_ID: int = int(get_env("API_ID")) # type: ignore
    API_HASH: str = get_env("API_HASH") # type: ignore

    MAIN_SESSION: str = get_env("MAIN_SESSION")  # type: ignore

    COMMAND_HANDLER: str = get_env("COMMAND_HANDLER", False, ".") # type: ignore

    TIME_ZONE: str = get_env("TIME_ZONE", False, "Asia/Kolkata") # type: ignore

    USERNAME: str|None = get_env("USERNAME", False)

    DB_CHAT_ID: int = get_env_int("DB_CHAT_ID", False) # type: ignore
    LOG_CHAT_ID: int|None = get_env_int("LOG_CHAT_ID", False)
    START_UP_CHAT_ID: int|None = get_env_int("START_UP_CHAT_ID", False)
    PLUGIN_CHANNEL_CHAT_ID: int|None = get_env("PLUGIN_CHANNEL_CHAT_ID", False) # type: ignore

    START_UP_TEXT: str = get_env("START_UP_TEXT", False, "Bot has started!") # type: ignore
    LOG_FILE_NAME: str = get_env("LOG_FILE_NAME", False, "Logs").strip(".log") + ".log" # type: ignore

    DEBUG: bool = get_env_bool("DEBUG", False)
    DEBUG_LOG_FILE_NAME: str = get_env("DEBUG_LOG_FILE_NAME", False, "debug").strip(".log") + ".log" # type: ignore

    SUDO_USERS: list[int] = [int(i) for i in get_env("SUDO_USERS", False, "").split(' ') if i.isdigit()] # type: ignore

    SESSION_STRINGS: list[str] = get_env("SESSION_STRINGS", False, "").split(' ') # type: ignore
    BOT_TOKENS: list[str] = get_env("BOT_TOKENS", False, "").split(' ') # type: ignore

    CUSTOM_DIRECTORIES: list[str] = get_env("CUSTOM_DIRECTORIES", False, "").split(' ') # type: ignore

    PLUGIN_NO_LOAD_APP: list[str] = get_env("PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    PLUGIN_NO_LOAD_BOT: list[str] = get_env("PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    # Conditional Statements and Fallbacks

    NAME = ""

    if USERNAME:
        NAME = USERNAME

    BOT_NAME = ""

    if MAIN_BOT_USERNAME:
        BOT_NAME = MAIN_BOT_USERNAME
    
    if SESSION_STRINGS == ['']:
        SESSION_STRINGS = []
    
    if BOT_TOKENS == ['']:
        BOT_TOKENS = []

    # Compounds:

    ALL_SESSION_STRINGS: list[str] = [MAIN_SESSION] + SESSION_STRINGS
    ALL_BOT_TOKENS: list[str] = [MAIN_BOT_TOKEN] + BOT_TOKENS

    # Post Start-Up Variables:

    APP_LOADED: bool = False
    BOT_LOADED: bool = False