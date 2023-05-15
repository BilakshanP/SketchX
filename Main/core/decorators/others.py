def monkeypatch(target):
    def decorator(func):
        setattr(target, func.__name__, func)

        return func

    return decorator