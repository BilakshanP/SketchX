from typing import Iterable

def is_present(substring: str, iterable: Iterable[str]):
    for string in iterable:
        if string is not None and substring in string:
            return True
    
    return False