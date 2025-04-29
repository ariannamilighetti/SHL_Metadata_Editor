import metadata_creator
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class From_Input(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.selection_frm = ttk.LabelFrame(self, text="Items details")
        self.selection_frm.pack(fill="x", padx=5, pady=5)
        self.row_count = 0
        self.input_fields('Input item(s) reference') # barcode
        self.input_fields( 'Title') # Title
        self.input_fields('Classmark') # Classmark
        self.input_fields('Catalogue Number') # Catalogue Number
        self.dropdown_field('Collection', 'collections_validation.txt') # Collection
        self.dropdown_field('Digitiser', 'digitiser_validation.txt') # Digitiser
        self.input_fields('Digitisation Date, yyyy-mm-dd') # Digitisation Date
        self.dropdown_field('Access Conditions', 'access_validation.txt') # Access Conditions
        self.dropdown_field('Restriction Reason', 'restriction_validation.txt') # Restriction Reason
        self.input_fields('Restriction Expiry Date, yyyy-mm-dd') # Restriction Exp Date
        self.dropdown_field('Copyright Status', 'copyright_validation.txt') # Copyright Status
        self.input_fields('Licence Details') # Licence Details

        self.folder_fileds()
        self.run_button()
        self.run_frame()
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight =1)
        self.selection_frm.columnconfigure(0, weight = 1)
        self.selection_frm.columnconfigure(1, weight = 0)
        self.selection_frm.columnconfigure(2, weight = 2)
    
    def input_fields(self, title):
        label = tk.Label(master=self.selection_frm, text=title, anchor='nw')
        input = tk.Entry(master=self.selection_frm, width = 50)
        label.grid(column=0, row=self.row_count, columnspan=1, sticky="nsew", padx=5, pady=5)
        input.grid(column=2, row=self.row_count, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.row_count += 1
    
    def dropdown_field(self, title, file):
        label = tk.Label(master=self.selection_frm, text=title, anchor='nw')
        entry = ttk.Combobox(master=self.selection_frm, width = 50, values = self.list_box_contents(file))
        label.grid(column=0, row=self.row_count, columnspan=1, sticky="nsew", padx=5, pady=5)
        entry.grid(column=2, row=self.row_count, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.row_count += 1

    def list_box_contents(self, file):
        data = []
        f = open(file,"r")
        for x in f:
            data.append(x)
        f.close()
        return data

    def folder_fileds(self):
        # Folder Fields
        dir_label = tk.Label(master=self.selection_frm, text="Select item(s) parent folder", anchor='nw')
        dir_button = tk.Button(self.selection_frm, text='Open', command=self.askDirectory_ss, bg='#ff8962')
        self.ss_directory_label = tk.Entry(master=self.selection_frm)
        dir_label.grid(column=0, row=2, columnspan=1, sticky="nsew", padx=5, pady=5)
        dir_button.grid(column=1, row=2, columnspan=1, sticky="nsew", padx=5, pady=5)
        self.ss_directory_label.grid(column=2, row=2, columnspan=3, sticky="nsew", padx=5, pady=5)

    def askDirectory_ss(self, event=None):
        global end_directory
        end_directory = filedialog.askdirectory()
        self.ss_directory_label.delete(0, "end")
        self.ss_directory_label.insert(0, end_directory)
    
    def run_button(self):
        run_button = tk.Button(self, text="Run", command=lambda: metadata_creator.__main__(), bg='#7fd1ae')
        run_button.pack(fill="x", padx=5, pady=5)
    
    def run_frame(self):
        # Running frame
        run_frame = ttk.LabelFrame(self, text="Running")
        run_shmark = tk.Label(master=run_frame, text="Item reference", anchor='nw')
        run_verification = tk.Label(master=run_frame, text="Metadata Validation", anchor='nw')
        run_status = tk.Label(master=run_frame, text="Status", anchor='nw')
        run_further_steps = tk.Label(master=run_frame, text="Further Steps", anchor='nw')

        run_frame.pack(fill="x", padx=5, pady=5)
        run_shmark.grid(column=0, row=0, sticky="nsew", padx=20, pady=5)
        run_verification.grid(column=1, row=0, sticky="nsew", padx=20, pady=5)
        run_status.grid(column=2, row=0, sticky="nsew", padx=20, pady=5)
        run_further_steps.grid(column=3, row=0, sticky="nsew", padx=20, pady=5)

# to test this class
def __main__():
    app = tk.Tk()
    tabs = ttk.Notebook(app)
    tabs.grid(row=1, column= 0, sticky="nsew")
    # Create Tabs
    data_input = From_Input()
    tabs.add(data_input, text='From Input')
    tk.mainloop()

if __name__ == '__main__':
    __main__()