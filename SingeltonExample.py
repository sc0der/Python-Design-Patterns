class Singleton:
    _instances = {}

    def __call__(cls, *a, **kw):
        if cls not in cls._instances:
            cls.__instances[cls] = super(Database, cls).__call__(cls, *a, **kw)
        return cls.__instances[cls]