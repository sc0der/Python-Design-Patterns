# Singleton
import random
'''
Singleton - subclassing can never be really smooth
• Use a module instead of a class (no inheritance, no special methods)
• make just one instance (self discipline, no enforcement), need to decide to “when” (in which
part if the code) to make it
• monostate (borg)

'''

class Database:
    __instance = None
    def __init__(self):
        id = random.randint(1, 101)
        print("id = ", id)

    def __new__(cls, *a, **kw):
        if not cls.__instance:
            cls.__instance = super(Database, cls).__new__(cls, *a, **kw)
        return cls.__instance
class Singleton(object):
    def __new__(cls, *a, **kw):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(*a, **kw)
        return cls._inst

# class Foo(Singleton): pass
# class Bar(Foo): pass
# f = Foo()
# b = Bar()

# singelton by decorator

def singelton(class_):
    instance = {}
    def get_instance(*a, **kw):
        if class_ not in instance:
            instance[class_] = class_(*a, **kw)
        return instance[class_]
    return get_instance

@singelton
class Database_:
    def __init__(self):
        id = random.randint(1, 101)
        print("id = ", id)

if __name__ == '__main__':
    d1 = Database_()
    d2 = Database_()
    print(d1 == d2)
# what class