import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Menu(object):
    def __init__(self, title, width=40):
        pass

    @property
    def app(self):
        pass

    @app.setter
    def app(self, app):
        pass

    @property
    def title(self):
        pass

    @title.setter
    def title(self, title):
        pass

    def add_item(self, item):
        pass

    def display(self):
        pass

    def run(self):
        pass

    def _navigate(self, choice):
        pass


class MenuItem(object):
    def __init__(self, title):
        pass

    @property
    def title(self):
        pass

    @title.setter
    def title(self, title):
        pass


class Application(object):
    def __init__(self, start_menu):
        pass

    @property
    def current_menu(self):
        pass

    @current_menu.setter
    def current_menu(self, menu_name):
        pass

    def add_menu(self, menu_name, menu):
        pass

    def run(self):
        pass
