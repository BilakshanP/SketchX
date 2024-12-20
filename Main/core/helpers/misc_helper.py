from typing import Iterable, Any

def is_present(substring: str, iterable: Iterable[str|None]):
    for string in iterable:
        if string is not None and substring in string:
            return True

    return False

def set_as_empty(iterable: list[Any]) -> list[Any]:
    if iterable == ['']:
        iterable = []

    return iterable