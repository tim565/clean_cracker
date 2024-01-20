import os
import tkinter as tk

from src.graphical_user_interface.graphical_user_interface import CleanCrackerGUI

# Enable relative imports from workspace/ -> Absolute file path not necessary
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_gui() -> None:
    root = tk.Tk()
    CleanCrackerGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run_gui()
