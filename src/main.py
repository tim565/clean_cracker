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


# TODO: Make demo File examples more impactful. Crack outpt file only contains one cracked password   TIM
# TODO: Complete Readme files with some basic instructions/overview. SO that prpose and functionality is easy to undestand   TIM
# TODO: Write testfunctions for files --->>> Make sure common forward is used:
#       Finished Completly: Adrian:  brute_force.py, generate_rainbow_table, utility_functions
#       Schmitz: crack_password_list.py, hash_cracker.py, hash_creator.py (only partly finished), security_auditing
