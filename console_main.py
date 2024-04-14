from console_base import *


class HotelMenu(Menu):
    def __init__(self, back):
        super().__init__("Hotel Management")
        self.add_option(MenuOption("View Hotels"))

        self._back = back
        self.add_option(MenuOption("Back"))

    def _navigate(self, choice: int):
        match choice:
            case 1:
                self.clear()
                print("View Hotels...")
                input("Press Enter to continue...")
                return self
            case 2:
                return self._back


class MainMenu(Menu):
    def __init__(self):
        super().__init__("Main Menu")
        self.add_option(MenuOption("Hotel Management"))
        self._hotel_menu = HotelMenu(self)

        self.add_option(MenuOption("Quit"))

    def _navigate(self, choice: int):
        match choice:
            case 1:
                return self._hotel_menu
            case 2:
                return None


if __name__ == "__main__":
    main_menu = MainMenu()
    app = Application(main_menu)
    app.run()