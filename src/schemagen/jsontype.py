

def jsontype(cls=None, *, only_local=False):
    if cls:
        cls.__json_args__ = {}
        return cls

    def wrap(cls):
        cls.__json_args__ = {"only_local": only_local}
        return cls

    return wrap


