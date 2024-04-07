import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Menu(object):
    def __init__(self, title, width=40):
        pass

    def get_app(self):
        pass

    def set_app(self, app):
        pass

    def get_title(self):
        pass

    def set_title(self, title):
        pass

    def get_with(self):
        pass

    def set_width(self, width):
        pass

    def add_item(self, item):
        pass

    def display(self):
        pass

    def run(self):
       pass

    def _navigate(self, choice):
        raise NotImplementedError()


class MenuItem(object):
    def __init__(self, title):
        pass

    def get_title(self):
        pass

    def set_title(self, title):
        pass

    def __len__(self):
        pass


class Application(object):
    def __init__(self, start_menu):
        pass

    def get_current_menu(self):
        pass

    def set_current_menu(self, menu_name):
        pass

    def add_menu(self, menu_name, menu):
        pass

    def run(self):
        clear_console()
        while True:
            pass
