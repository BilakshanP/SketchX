import pytz

from os import path, mkdir, getenv
from traceback import format_exc
from datetime import datetime as _datetime
from dotenv import load_dotenv as _load_dotenv

_load_dotenv()

_tz = pytz.timezone(getenv("TIME_ZONE", "Asia/Kolkata"))

def time() -> str:
    return _datetime.now(_tz).strftime('%a %b %d %H:%M:%S %Y')

if not path.exists("Logs/"):
    mkdir("Logs/")


def generic_logger(
        message: str, type: str, symbol: str, save_to_file: bool = True,
        append: str = "", new_line: bool = True, silence: bool = False):

    nl = "\n" if new_line else ""
    file_name = "Logs/" + type.lower() + ".log"

    if not silence:
        print(f"{append}[{symbol}]: {message}", end = nl)

    if save_to_file:
        text: str = f"{append}[{type}] @ {time()} {symbol} {message}{nl}"

        with open(file_name, "a") as file:
            file.write(text)

        with open("Logs/logs.log", "a") as file:
            file.write(text)


def info(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "INFO", "+", True, append, new_line, silence)

def warn(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "WARN", "~", True, append, new_line, silence)

def error(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "ERROR", "-", True, append, new_line, silence)

def debug(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    generic_logger(message, "DEBUG", "~", True, append, new_line, silence)

def exception(message: str, append: str = "", new_line: bool = True, silence: bool = False):
    traceback = append + "     " + format_exc().replace("\n", "\n" + append + "     ")
    generic_logger(message + "\n" + traceback, "EXCEPTION", "#", True, append, new_line, silence)

def empty():
    print()

    with open("Logs/logs.log", "a") as file:
        file.write("\n")