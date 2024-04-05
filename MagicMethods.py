class Person(object):
    def __init__(self, firstname, lastname, size):
        self._firstname = firstname
        self._lastname = lastname
        self._size = size

    def __repr__(self):
        return f"Person({self._firstname}, {self._lastname}, {self._size})"

    def __str__(self):
        return f"Mein Name ist {self._firstname} {self._lastname} und ich bin {self._size} cm gross."

    def __len__(self):
        return self._size


if __name__ == '__main__':
    hotel_1 = "Hotel Aria"
    hotel_2 = "Hotel Amaris"
    hotel_3 = "Leonardo Boutique Hotel Rigihof Zurich"
    print(hotel_1)
    print(len(hotel_1))

    hotel_list = ["Hotel Aria", "Hotel Amaris", "Leonardo Boutique Hotel Rigihof Zurich"]
    print(hotel_list)
    print(type(hotel_list))
    print(len(hotel_list))

    p = Person("Phillip", "Gachnang", 177)
    print(repr(p))
    print(p)
    print(len(p))


