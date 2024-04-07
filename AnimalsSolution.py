class Animal(object):
    def __init__(self, species: str):
        self.__species = species

    def get_species(self):
        return self.__species

    def make_sound(self):
        raise NotImplementedError("You must implement make_sound")

    def who_am_i(self):
        print(f"I am an {type(self)}, with the species {self.get_species()}")
        print(f"I make", end=" ")
        self.make_sound()


class Pet(Animal):
    def __init__(self, species: str, name: str, owner: str = None):
        super().__init__(species)
        self._name = name
        self._owner = owner

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner


class Dog(Pet):
    def __init__(self, name: str, owner: str = None):
        super().__init__("Dog", name, owner)

    def make_sound(self):
        print("woof")

    def go_for_a_walk(self):
        print("walk")

    def who_am_i(self):
        super().who_am_i()
        print(f"I love to", end=" ")
        self.go_for_a_walk()


class Cat(Pet):
    def __init__(self, name, owner: str = None):
        super().__init__("Cat", name, owner)

    def make_sound(self):
        print("meow")

    def groom(self):
        print("groom")

    def who_am_i(self):
        super().who_am_i()
        print(f"I love to", end=" ")
        self.groom()

    def __str__(self):
        return f"I am a cat called {self._name}"


if __name__ == '__main__':
    animal = Animal("test")
    # animal.make_sound()

    chilli = Dog("Chilli", "Samuel")
    chilli.who_am_i()
    print(chilli.get_name())
    print(chilli.get_owner())
    print(chilli)

    kimi = Cat("Kimi", "Phillip")
    kimi.who_am_i()
    print(kimi.get_name())
    print(kimi.get_owner())
    print(kimi)


    variable = "String"