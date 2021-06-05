from tkinter import Tk, Label, Button, Entry, X

import tkinter
from tkinter import ttk
from tkinter import messagebox


class Root(Tk):
    def __init__(self):
        super().__init__()

        for x in [ttk.Label, ttk.Button, ttk.Entry, ttk.Checkbutton, ttk.Radiobutton]:
            x(self, text='Some ' + x.__name__).pack(fill=X)
        pb = ttk.Progressbar(self, length=100)
        pb.pack(fill=X)
        pb.step(33)

        ttk.Label(self, text='Select theme:').pack(pady=[50, 10])

        self.style = ttk.Style()
        self.combo = ttk.Combobox(self, values=self.style.theme_names())
        self.combo.pack(pady=[0, 10])
        button = ttk.Button(self, text='Apply')
        button['command'] = self.change_theme
        button.pack(pady=10)

    def change_theme(self):
        content = self.combo.get()
        try:
            self.style.theme_use(content)
        except:
            print("Failed to set theme " + content)


root = Root()
root.mainloop()
