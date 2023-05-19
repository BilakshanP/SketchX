import time as _time

from Main.core.helpers.logging_helper import debug as _debug

def timer(func, append: str = ""):
    def wrapper(*args, **kwargs):
        start_time = _time.time()
        result = func(*args, **kwargs)
        end_time = _time.time()
        execution_time = end_time - start_time
        _debug(f"Execution time of {func.__name__} in {func.__module__}: {execution_time:.6f} seconds", append)
        return result
    return wrapper
