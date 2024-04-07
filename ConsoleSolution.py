import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Menu(object):
    def __init__(self, title, width=40):
        self._app = None
        self._title = title
        self._width = width
        self._items = []

    def get_app(self):
        return self._app

    def set_app(self, app):
        self._app = app

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_with(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def add_item(self, item):
        self._items.append(item)

    def display(self):
        print("#" * self._width)
        spaces_needed = self._width - len(self._title) - 2 - 3
        print("#", self._title, " " * spaces_needed, "#")
        print("#" * self._width)

        for i, item in enumerate(self._items):
            num_as_str = str(i + 1) + "."
            spaces_needed = self._width - len(num_as_str) - len(item) - 2 - 4
            print("#", f"{num_as_str}", item.get_title(), " " * spaces_needed, "#")
        print("#" * self._width)

    def run(self):
        possible_choices = [str(i + 1) for i in range(len(self._items))]
        user_choice = None
        while user_choice not in possible_choices:
            clear_console()
            self.display()
            if user_choice is not None:
                print("Invalid choice")
            user_choice = input("Select: ")
        self._navigate(user_choice)

    def _navigate(self, choice):
        raise NotImplementedError()


class MenuItem(object):
    def __init__(self, title):
        self.set_title(title)

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def __len__(self):
        return len(self._title)


class Application(object):
    def __init__(self, start_menu):
        self._current_menu = start_menu
        self._menus = {}

    def get_current_menu(self):
        return self._current_menu

    def set_current_menu(self, menu_name):
        self._current_menu = self._menus[menu_name]

    def add_menu(self, menu_name, menu):
        self._menus[menu_name] = menu
        menu.set_app(self)

    def run(self):
        clear_console()
        while True:
            self._current_menu.run()
