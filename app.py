import rumps
from Functions import Functions


class SortiumApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Sortium",
            "sort": "Sort items",
            "favorite": "Add to Favorites",
            "unfavorite": "Remove from Favorites",
            "settings": "settings"
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.sort_button = rumps.MenuItem(title=self.config["sort"], callback=self.sort_items)
        self.fav_button = rumps.MenuItem(title=self.config["favorite"], callback=self.add_rem_favbar)
        self.settings_button = rumps.MenuItem(title=self.config["settings"], callback=self.settings)
        self.app.menu = [self.sort_button, self.fav_button]

    def set_up_menu(self):
        self.app.title = "🔘"

    def sort_items(self, sender):
        func = Functions()
        if sender.title == self.config["sort"]:
            func.sort(func.file_type, func.file_destination)
        self.sort_items()

    def add_rem_favbar(self, sender):
        func = Functions()
        if sender.title == self.config["favorite"]:
            func.add_sideBar()
            sender.title = self.config["unfavorite"]
        else:
            func.rem_sideBar()
            sender.title = self.config["favorite"]

    def settings(self, sender):
        func = Functions()
        func.settings_window()

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = SortiumApp()
    app.run()
