class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Cũng tùy loài mà kêu...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} kêu: Gâu Gâu!")

my_dog = Dog("Lulu")
my_dog.sound()
