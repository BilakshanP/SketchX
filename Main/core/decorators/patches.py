from typing import Type, Callable, Any
import types

def monkeypatch(parent_class: Type[Any]) -> Callable[[Type[Any]], Type[Any]]:
    """
    A decorator that monkey patches the methods of the surrogate class into the parent class.

    Args:
        parent_class (Type[Any]): The class to be monkey patched.

    Returns:
        Callable[[Type[Any]], Type[Any]]: A decorator function that applies the monkey patch.
    """
    def wrapper(surrogate_class: Type[Any]) -> Type[Any]:
        for func_name, func in surrogate_class.__dict__.items():
            if func_name[:2] != "__" and isinstance(func, types.FunctionType):
                setattr(parent_class, func_name, func)
        return surrogate_class

    return wrapper
