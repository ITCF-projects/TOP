

def jsontype(cls=None, *, python_type: type = None):
    if cls:
        cls.__json_args__ = {"python_type": python_type}
        return cls

    def wrap(cls):
        cls.__json_args__ = {"python_type": python_type}
        return cls

    return wrap


