 # type: ignore

def monkeypatch(parent_class):
    def wrapper(surrogate_class):
        for (func_name, func) in surrogate_class.__dict__.items():
            if func_name[:2] != "__":
                setattr(parent_class, func_name, func)
        return surrogate_class

    return wrapper