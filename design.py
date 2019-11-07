import tkinter as tk


class Page(tk.Frame):
    def __init__(self, app, root, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.app = app
        self.root = root
        self.height = None
        self.width = None
        self.title = None

    def show(self):
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.root.title(self.title)
        self.lift()

    def start(self):
        self.app.add_page(self)


