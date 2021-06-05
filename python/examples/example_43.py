from tkinter import Tk, Label


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Hello, world!")
        self.label.pack()


root = Root()
root.mainloop()
