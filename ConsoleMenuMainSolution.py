import sys
from types import MethodType

import ConsoleSolution as Console


class MainMenu(Console.Menu):
    def __init__(self):
        super().__init__("Main Menu")

    def _navigate(self, choice):
        match choice:
            case '1':
                self.app.current_menu = "hotel_menu"
            case '2':
                self.app.current_menu = "reservation_menu"
            case '3':
                sys.exit(0)


class HotelMenu(Console.Menu):
    def __init__(self):
        super().__init__("Hotel Management")


def hotel_nav(self, choice):
    match choice:
        case '1':
            Console.clear_console()
            print("User selected 1 to add a new hotel")
            input()
            self.app.current_menu = "hotel_menu"
        case '2':
            self.app.current_menu = "main_menu"

def reservation_nav(self, choice):
    match choice:
        case '1':
            Console.clear_console()
            print("User selected 1 to view reservations")
            input()
            self.app.current_menu = "reservation_menu"
        case '2':
            self.app.current_menu = "main_menu"


if __name__ == "__main__":

    # override method in new class
    main_menu = MainMenu()
    main_menu.add_choice(Console.MenuItem("Hotel Management"))
    main_menu.add_choice(Console.MenuItem("Reservations"))
    main_menu.add_choice(Console.MenuItem("Quit"))

    # override method dynamically on class
    HotelMenu._navigate = hotel_nav
    hotel_menu = HotelMenu()
    hotel_menu.add_choice(Console.MenuItem("Add new Hotel"))
    hotel_menu.add_choice(Console.MenuItem("Back"))

    # override method dynamically on object
    reservation_menu = Console.Menu("Reservations")
    reservation_menu._navigate = MethodType(reservation_nav, reservation_menu)
    reservation_menu.add_choice(Console.MenuItem("View Reservations"))
    reservation_menu.add_choice(Console.MenuItem("Back"))

    app = Console.Application(main_menu)
    app.add_menu("main_menu", main_menu)
    app.add_menu("hotel_menu", hotel_menu)
    app.add_menu("reservation_menu", reservation_menu)

    while True:
        app.run()