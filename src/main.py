import os
import sys

# Enable relative imports from workspace/ -> Absolute file path not necessary
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.graphical_user_interface.graphical_user_interface import CleanCrackerGUI

import tkinter as tk



def run_gui():
    root = tk.Tk()
    app = CleanCrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()


# TODO: Add Type Anotation
# TODO: Make demo File examples more impactful
