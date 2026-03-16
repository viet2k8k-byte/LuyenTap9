class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))

    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}"
p = Person.from_string("Nam-20")
print(p)


