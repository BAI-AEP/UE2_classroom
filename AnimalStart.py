class Animal(object):
    def __init__(self):
        pass

    def make_sound(self):
        raise NotImplementedError("You must implement make_sound")

class Pet(Animal):
    def __init__(self):
        pass


class Dog(Pet):
    def __init__(self):
        pass

class Cat(Pet):
    def __init__(self):
        pass


if __name__ == '__main__':
    animal = Animal("Bird")
    animal.make_sound()