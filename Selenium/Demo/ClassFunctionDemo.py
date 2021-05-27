class MyClass:
    name = "Michael"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)

x = MyClass('John', 40)
print(x.name)
x.sum(4,5)
print(x.age)
del x.name
print(x.age)