class Animal(object):
    def __init__(self, species: str):
        self.__species = species

    @property
    def species(self):
        return self.__species

    def make_sound(self):
        raise NotImplementedError("You must implement make_sound")


class Pet(Animal):
    def __init__(self, species: str, name: str, owner: str = None):
        super().__init__(species)
        self._name = name
        self._owner = owner

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner


class Dog(Pet):
    def __init__(self, name: str, owner: str = None):
        super().__init__("Dog", name, owner)

    def make_sound(self):
        print("woof")

    def go_for_a_walk(self):
        print("walk")


class Cat(Pet):
    def __init__(self, name, owner: str = None):
        super().__init__("Cat", name, owner)

    def make_sound(self):
        print("meow")

    def groom(self):
        print("groom")

    def __str__(self):
        return f"I am a cat called {self.name}"


if __name__ == '__main__':
    animal = Animal("test")
    # animal.make_sound()

    chilli = Dog("Chilli", "Samuel")
    chilli.make_sound()
    chilli.go_for_a_walk()
    print(chilli.name)
    print(chilli.owner)
    print(chilli)

    kimi = Cat("Kimi", "Phillip")
    kimi.make_sound()
    kimi.groom()
    print(kimi.name)
    print(kimi.owner)
    print(kimi)


    variable = "String"