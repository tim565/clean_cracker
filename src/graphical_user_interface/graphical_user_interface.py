import tkinter as tk
from tkinter import ttk
import traceback

from src.crack_functionalities.brute_force import brute_force
from src.crack_functionalities.crack_password_list import crack_password_list
from src.crack_functionalities.hash_creator import hash_string


class CleanCrackerGUI:
    """
    A GUI application for creating rainbow tables, cracking hashes, generating hashes, and brute forcing hashes.
    """

    def __init__(self, root):
        """
        Initializes the CleanCrackerGUI class.

        Parameters:
        - root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Clean Cracker")
        self.root.geometry("900x600")
        self.background_color = '#F0F0F0'
        self.root.configure(background=self.background_color)

        self.setup_gui_left_side()
        self.setup_gui_right_side()


    def setup_gui_left_side(self):
        """
        Sets up the left side of the GUI, including the Create Rainbow Table and Crack Hashes sections.
        """
        # Create frame for left side
        left_frame = tk.Frame(self.root, background=self.background_color)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Section: Create Rainbow Table
        tk.Label(left_frame, text="Create Rainbow Table", bg=self.background_color, font=("Arial", 15)).pack(
            pady=(20, 10))
        self.csv_path_entry = tk.Entry(left_frame, width=40)
        self.add_placeholder(self.csv_path_entry, "CSV Path")
        self.csv_path_entry.pack(pady=(0, 10))

        self.hashing_algorithm_var = tk.StringVar()
        hashing_algorithm = ttk.OptionMenu(left_frame, self.hashing_algorithm_var, "md5", "sha1", "sha224", "sha256",
                                           "sha384", "sha512")
        hashing_algorithm.pack(pady=(0, 10))

        create_button = tk.Button(left_frame, text="Create", command=self.create_rainbow_table)
        create_button.pack(pady=(0, 10))

        self.status_create_label = tk.Label(left_frame, text="", bg=self.background_color)
        self.status_create_label.pack(pady=(0, 10))

        # Section: Crack Hashes Section
        tk.Label(left_frame, text="Crack Hashes", bg=self.background_color, font=("Arial", 15)).pack(pady=(45, 10))
        self.csv_path_rainbow_entry = tk.Entry(left_frame, width=40)
        self.add_placeholder(self.csv_path_rainbow_entry, "CSV Path Rainbow Table")
        self.csv_path_rainbow_entry.pack(pady=(0, 10))

        self.csv_path_hashes_entry = tk.Entry(left_frame, width=40)
        self.add_placeholder(self.csv_path_hashes_entry, "CSV Path Hashes to Crack")
        self.csv_path_hashes_entry.pack(pady=(0, 10))

        crack_button = tk.Button(left_frame, text="Crack", command=self.crack_hashes)
        crack_button.pack(pady=(0, 10))

        self.status_crack_label = tk.Label(left_frame, text="", bg=self.background_color)
        self.status_crack_label.pack(pady=(0, 10))


    def setup_gui_right_side(self):
        """
        Sets up the right side of the GUI, including the Generate Hash and Brute Force sections.
        """
        # Create frame for right side
        right_frame = tk.Frame(self.root, background=self.background_color)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Section: Generate Hash
        tk.Label(right_frame, text="Generate Hash", bg=self.background_color, font=("Arial", 15)).pack(pady=(20, 10))
        self.raw_string_entry = tk.Entry(right_frame)
        self.add_placeholder(self.raw_string_entry, "Raw String")
        self.raw_string_entry.pack(pady=(0, 10))

        self.hash_algo_raw_var = tk.StringVar()
        hash_algo_raw = ttk.OptionMenu(right_frame, self.hash_algo_raw_var, "md5", "sha1", "sha224", "sha256", "sha384",
                                       "sha512")
        hash_algo_raw.pack(pady=(0, 10))

        generate_button = tk.Button(right_frame, text="Generate Hash", command=self.generate_hash_string)
        generate_button.pack(pady=(0, 10))

        self.status_create_text = tk.Text(right_frame, height=4, width=50, bg=self.background_color, wrap="word",
                                          borderwidth=0, highlightthickness=0)
        self.status_create_text.pack(pady=(0, 10))
        self.status_create_text.insert("1.0", "")  # Initially empty
        self.status_create_text.configure(state="disabled",
                                          inactiveselectbackground=self.status_create_text.cget("selectbackground"))

        # Section: Brute Force
        tk.Label(right_frame, text="Brute Force", bg=self.background_color, font=("Arial", 15)).pack(pady=(0, 10))
        self.hash_string_entry = tk.Entry(right_frame, width=50)
        self.add_placeholder(self.hash_string_entry, "Hash String")
        self.hash_string_entry.pack(pady=(0, 10))

        self.length_entry = tk.Entry(right_frame)
        self.add_placeholder(self.length_entry, "Max Password Length")
        self.length_entry.pack(pady=(0, 10))

        self.include_digits_var = tk.BooleanVar()
        include_digits_frame = tk.Frame(right_frame, background=self.background_color)
        include_digits_label = tk.Label(include_digits_frame, text="Include Digits", bg=self.background_color)
        include_digits_yes = tk.Radiobutton(include_digits_frame, text="Yes", variable=self.include_digits_var,
                                            value=True, bg=self.background_color)
        include_digits_no = tk.Radiobutton(include_digits_frame, text="No", variable=self.include_digits_var,
                                           value=False, bg=self.background_color)
        include_digits_label.pack(side=tk.LEFT)
        include_digits_yes.pack(side=tk.LEFT)
        include_digits_no.pack(side=tk.LEFT)
        include_digits_frame.pack(pady=(0, 10))

        self.include_special_var = tk.BooleanVar()
        include_special_frame = tk.Frame(right_frame, background=self.background_color)
        include_special_label = tk.Label(include_special_frame, text="Include Special Characters",
                                         bg=self.background_color)
        include_special_yes = tk.Radiobutton(include_special_frame, text="Yes", variable=self.include_special_var,
                                             value=True, bg=self.background_color)
        include_special_no = tk.Radiobutton(include_special_frame, text="No", variable=self.include_special_var,
                                            value=False, bg=self.background_color)
        include_special_label.pack(side=tk.LEFT)
        include_special_yes.pack(side=tk.LEFT)
        include_special_no.pack(side=tk.LEFT)
        include_special_frame.pack(pady=(0, 10))

        start_button = tk.Button(right_frame, text="Start Brute Forcing", command=self.brute_force_hash)
        start_button.pack(pady=(0, 10))

        self.result_label = tk.Label(right_frame, text="", bg=self.background_color)
        self.result_label.pack(pady=(0, 10))


    def generate_hash_string(self):
        """
        Generates a hash string based on the raw string and selected hashing algorithm.
        """
        try:
            raw_string = self.raw_string_entry.get()
            algorithm = self.hash_algo_raw_var.get()
            print(f"Creating hash with {algorithm} for string {raw_string}")
            hashed_string = hash_string(raw_string, hash_algorithm=algorithm)
            self.update_status_create("Finished! Hashed String: " + hashed_string)
        except Exception as e:
            print(traceback.format_exc())
            self.update_status_create("Error")


    def create_rainbow_table(self):
        """
        Creates a rainbow table based on the selected CSV file and hashing algorithm.
        """
        try:
            csv_path = self.csv_path_entry.get()
            algorithm = self.hashing_algorithm_var.get()
            print(f"Creating rainbow table with {algorithm} for file {csv_path}")
            self.status_create_label.config(text="Finished")
        except Exception as e:
            print(traceback.format_exc())
            self.status_create_label.config(text="Error")


    def crack_hashes(self):
        """
        Cracks hashes using the selected rainbow table and CSV file.
        """
        try:
            csv_path_rainbow = self.csv_path_rainbow_entry.get()
            csv_path_hashes = self.csv_path_hashes_entry.get()
            print(f"Cracking hashes from {csv_path_hashes} using rainbow table {csv_path_rainbow}")
            crack_password_list(csv_path_rainbow, csv_path_hashes, "sha256")
            self.status_crack_label.config(text="Finished")
        except Exception as e:
            print(traceback.format_exc())
            self.status_crack_label.config(text="Error")


    def brute_force_hash(self):
        """
        Performs brute force attack on a hash string using the selected parameters.
        """
        try:
            hash_string = self.hash_string_entry.get()
            max_pw_length = int(self.length_entry.get())
            include_digits = self.include_digits_var.get()
            include_special = self.include_special_var.get()
            print(f"Started brute forcing hash {hash_string} with length {max_pw_length}, digits: {include_digits}, special: {include_special}")
            success, password = brute_force(max_pw_length, hash_string, include_digits, include_special)
            if success:
                self.result_label.config(text="Finished! The password is: " + password)
            else:
                self.result_label.config(text="Finished! The password could not be determined.")
        except Exception as e:
            print(traceback.format_exc())
            self.result_label.config(text="Error")


    def on_entry_click(self, event, entry, default_text):
        """
        Handles the event when an entry field is clicked.

        Parameters:
        - event (tk.Event): The event object.
        - entry (tk.Entry): The entry field that was clicked.
        - default_text (str): The default text of the entry field.
        """
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')


    def on_focusout(self, event, entry, default_text):
        """
        Handles the event when an entry field loses focus.

        Parameters:
        - event (tk.Event): The event object.
        - entry (tk.Entry): The entry field that lost focus.
        - default_text (str): The default text of the entry field.
        """
        if entry.get() == '':
            entry.insert(0, default_text)
            entry.config(fg='grey')


    def add_placeholder(self, entry, text):
        """
        Adds a placeholder text to an entry field.

        Parameters:
        - entry (tk.Entry): The entry field to add the placeholder to.
        - text (str): The placeholder text.
        """
        entry.insert(0, text)
        entry.config(fg='grey')
        entry.bind("<FocusIn>", lambda event, e=entry, t=text: self.on_entry_click(event, e, t))
        entry.bind("<FocusOut>", lambda event, e=entry, t=text: self.on_focusout(event, e, t))


    def update_status_create(self, text):
        """
        Updates the status text in the Create Hash section.

        Parameters:
        - text (str): The new status text.
        """
        self.status_create_text.configure(state="normal")
        self.status_create_text.delete("1.0", tk.END)
        self.status_create_text.insert("1.0", text)
        self.status_create_text.configure(state="disabled")
