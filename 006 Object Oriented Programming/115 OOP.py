from ast import Pass


class human():
    # class object attribute or static attribute
    Name = ''

    def __init__(self, param1):
        self.param1 = param1  # attributes

    @staticmethod
    def method1():
        Pass

    @classmethod
    def method2(cls):
        Pass


class indian(human):
    def __init__(self, location, param1):
        super().__init__(param1)
        Pass


class american(human):
    def __init__(self, location, param1):
        super().__init__(param1)
        Pass


class indoAmerican(indian, american):
    Pass


print(indoAmerican.mro())
