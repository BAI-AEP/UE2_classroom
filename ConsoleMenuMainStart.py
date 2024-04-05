import sys
from types import MethodType

import ConsoleStart as Console


class MainMenu(Console.Menu):
    def __init__(self):
        super().__init__("Main Menu")

    def _navigate(self, choice):
        pass


class HotelMenu(Console.Menu):
    def __init__(self):
        super().__init__("Hotel Management")


def hotel_nav(self, choice):
    pass

def reservation_nav(self, choice):
    pass


if __name__ == "__main__":

    # override method in new class
    main_menu = MainMenu()
    main_menu.add_item(Console.MenuItem("Hotel Management"))
    main_menu.add_item(Console.MenuItem("Reservations"))
    main_menu.add_item(Console.MenuItem("Quit"))

    # override method dynamically on class
    HotelMenu._navigate = hotel_nav
    hotel_menu = HotelMenu()
    hotel_menu.add_item(Console.MenuItem("Add new Hotel"))
    hotel_menu.add_item(Console.MenuItem("Back"))

    # override method dynamically on object
    reservation_menu = Console.Menu("Reservations")
    reservation_menu._navigate = MethodType(reservation_nav, reservation_menu)
    reservation_menu.add_item(Console.MenuItem("View Reservations"))
    reservation_menu.add_item(Console.MenuItem("Back"))

    app = Console.Application(main_menu)
    app.add_menu("main_menu", main_menu)
    app.add_menu("hotel_menu", hotel_menu)
    app.add_menu("reservation_menu", reservation_menu)

    app.run()
