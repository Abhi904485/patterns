class Person:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, name):
        if name.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,name)

    def __getattr__(self, name):
        return self.__dict__.get(name, "Abhishek")


p1 = Person("abcd")

print(p1.current)
