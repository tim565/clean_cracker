import tkinter as tk

from src.graphical_user_interface.graphical_user_interface import CleanCrackerGUI


def run_gui():
    root = tk.Tk()
    app = CleanCrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
