import os
import tkinter as tk

from src.graphical_user_interface.graphical_user_interface import CleanCrackerGUI

# Enable relative imports from workspace/ -> Absolute file path not necessary
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_gui():
    root = tk.Tk()
    CleanCrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()

# TODO: Add Type Anotation
# TODO: Make demo File examples more impactful
# TODO: Complete Readme files with some basic instructions/overview
# TODO: Check whether this global variable SUPORTED_ALGORYTHMS is always used from configurations.py
# TODO: Determine the difference between both functions and check whether they are actually necessary in hash_creator.py
# TODO: String currently use "" and ''. We should only use one style. Lets use ''. If you adapt the "" make sure that
#  the code is still working afterwards.
