from console_base import *


class HotelMenu(Menu):
    pass


class MainMenu(Menu):
    pass


if __name__ == "__main__":
    main_menu = MainMenu()
    app = Application(main_menu)
    app.run()