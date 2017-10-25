class PageRegister(object):
    registry = {}

    @classmethod
    def register(cls, name=None):
        def decorator(f):
            _name = name # nonlocal
            if _name is None:
                _name = f.__name__
            if _name in cls.registry:
                raise KeyError('PageRegister: Duplicate registry')
            cls.registry[_name] = f
            return f
        return decorator

    @classmethod
    def pages(cls):
        return cls.registry