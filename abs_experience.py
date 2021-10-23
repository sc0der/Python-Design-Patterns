from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def foo(self):
        print("base foo")
        
    @abstractmethod
    def bar(self, value):
        return value * 2
        
        
class Real(Base):
    def foo(self):
        print("real foo")

    def bar(self, value):
        print("real bar", value)

    def other(self):
        print("other method")

r = Real("Koko")

print(r.name)
r.foo()
r.bar(3)
