import os


class Console(object):
    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError("Implement this method")

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


class Application(object):

    def __init__(self, start: Console):
        self._current: Console = start

    def run(self):
        pass


class MenuOption(object):
    def __init__(self, title):
        self._title = title

    def get_title(self) -> str:
        return self._title

    def __str__(self):
        return self._title

    def __len__(self):
        return len(self._title)


class Menu(Console):
    def __init__(self, title, width=50):
        super().__init__()
        self._title = title
        self._options = []
        self._width = width

    def __iter__(self):
        pass

    def get_options(self) -> list:
        pass

    def add_option(self, option: MenuOption):
        pass

    def remove_option(self, option: MenuOption):
        pass

    def show(self):
        pass

    def run(self) -> Console:
        pass

    def make_choice(self) -> int:
        pass

    def _navigate(self, choice: int):
        raise NotImplementedError("Implement this method")
