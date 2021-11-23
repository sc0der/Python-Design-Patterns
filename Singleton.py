# Singleton
'''
Singleton - subclassing can never be really smooth
• Use a module instead of a class (no inheritance, no special methods)
• make just one instance (self discipline, no enforcement), need to decide to “when” (in which
part if the code) to make it
• monostate (borg)

'''

class Singleton(object):
    def __new__(cls, *a, **kw):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(*a, **kw)
        return cls._inst

class Foo(Singleton): pass
class Bar(Foo): pass
f = Foo()
b = Bar()
# what class