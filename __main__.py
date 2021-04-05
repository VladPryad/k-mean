import tkinter as tk
from components.tabcontrol import Tabcontrol


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.tabcontrol = Tabcontrol(self)

        self.tabcontrol.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()