import pytz

from os import path, mkdir, getenv
from traceback import format_exc
from datetime import datetime as _datetime
from dotenv import load_dotenv as _load_dotenv

_load_dotenv()

_tz = pytz.timezone(getenv("TIME_ZONE", "Asia/Kolkata"))

def time() -> str:
    return _datetime.now(_tz).strftime("%d-%m-%Y %H:%M:%S")

if not path.exists("logs/"):
    mkdir("logs/")

def exception_traceback_formatter(append: str):
    return append + "     " + format_exc().replace("\n", "\n" + append + "     ")

def generic_logger(
        message: str, type: str, symbol: str, save_to_file: bool = True,
        append: str = "", new_line: bool = True, silence: bool = False):

    nl = "\n" if new_line else ""
    file_name = "logs/" + type.lower() + ".log"

    if not silence:
        print(f"[{symbol}]: {append}{message}", end = nl)

    if save_to_file:
        text: str = f"[{type}] @ {time()} {symbol} {append} {message}{nl}"

        with open(file_name, "a") as file:
            file.write(text)

        with open("logs/logs.log", "a") as file:
            file.write(text)

def info(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "INFO", "+", True, append, new_line, silence)

def warn(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "WARN", "~", True, append, new_line, silence)

def error(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "ERRR", "-", True, append, new_line, silence)

def debug(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "DEBG", "~", True, append, new_line, silence)

def exception(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message + "\n" + exception_traceback_formatter(append), "EXCEPTION", "#", True, append, new_line, silence)

def empty():
    print("[ ]: ")

    with open("logs/logs.log", "a") as file:
        file.write(f"[    ] @ {time()}\n")