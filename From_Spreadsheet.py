import metadata_creator
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class From_Spreadsheet (ttk.Frame):

    def __init__(self):
        super().__init__()
        self.selection_frm = ttk.LabelFrame(self, text="Items")
        self.selection_frm.grid(row=0, column=0, sticky='nwse', padx=5, pady=5)
        self.barcode_fields()
        self.spreadsheeet_filed()
        self.folder_fileds()
        self.run_button()
        self.run_frame()
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight =0)
        self.selection_frm.columnconfigure(0, weight = 1)
        self.selection_frm.columnconfigure(1, weight = 0)
        self.selection_frm.columnconfigure(2, weight = 2)


    def barcode_fields(self):
        # Barcode Fields
        barcode_label = tk.Label(master=self.selection_frm, text="Input item(s) reference", anchor='nw')
        barcode_number = tk.Entry(master=self.selection_frm, width = 50)
        barcode_label.grid(column=0, row=0, columnspan=1, sticky="ew", padx=5, pady=5)
        barcode_number.grid(column=2, row=0, columnspan=3, sticky="ew", padx=5, pady=5)

    def spreadsheeet_filed(self):
        # Spreadsheet Fields
        spreadsheet_label = tk.Label(master=self.selection_frm, text="Import metadata spreadsheet", anchor='nw')
        spreadsheet_button = tk.Button(self.selection_frm, text='Open', command=self.upload_spreadsheet,bg='#ff8962')
        self.spreadsheet_filename = tk.Entry(master=self.selection_frm)
        spreadsheet_label.grid(column=0, row=1, columnspan=1, sticky="ew", padx=5, pady=5)
        spreadsheet_button.grid(column=1, row=1, columnspan=1, sticky="ew", padx=5, pady=5)
        self.spreadsheet_filename.grid(column=2, row=1, columnspan=3, sticky="ew", padx=5, pady=5)
    
    def folder_fileds(self):
        # Folder Fields
        dir_label = tk.Label(master=self.selection_frm, text="Select item(s) parent folder", anchor='nw')
        dir_button = tk.Button(self.selection_frm, text='Open', command=self.askDirectory_ss, bg='#ff8962')
        self.ss_directory_label = tk.Entry(master=self.selection_frm)
        dir_label.grid(column=0, row=2, columnspan=1, sticky="ew", padx=5, pady=5)
        dir_button.grid(column=1, row=2, columnspan=1, sticky="ew", padx=5, pady=5)
        self.ss_directory_label.grid(column=2, row=2, columnspan=3, sticky="ew", padx=5, pady=5)

    def run_button(self):
        run_button = tk.Button(self, text="Run", command=lambda: metadata_creator.__main__(), bg='#7fd1ae')
        run_button.grid(row=1, column=0, sticky='nwse', padx=5, pady=5)
    
    def run_frame(self):
        # Running frame
        run_frame = ttk.LabelFrame(self, text="Running")
        run_shmark = tk.Label(master=run_frame, text="Item reference", anchor='nw')
        run_verification = tk.Label(master=run_frame, text="Metadata Validation", anchor='nw')
        run_status = tk.Label(master=run_frame, text="Status", anchor='nw')
        run_further_steps = tk.Label(master=run_frame, text="Further Steps", anchor='nw')

        run_frame.grid(row=2, column=0, sticky='nwse', padx=5, pady=5)
        run_shmark.grid(column=0, row=0, sticky="ew", padx=20, pady=5)
        run_verification.grid(column=1, row=0, sticky="ew", padx=20, pady=5)
        run_status.grid(column=2, row=0, sticky="ew", padx=20, pady=5)
        run_further_steps.grid(column=3, row=0, sticky="ew", padx=20, pady=5)

    def upload_spreadsheet (self,event=None):
        global spreadsheet_input
        spreadsheet_input = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("Any file", "*")))
        self.spreadsheet_filename.delete(0, "end")
        self.spreadsheet_filename.insert(0, spreadsheet_input)

    def askDirectory_ss(self, event=None):
        global end_directory
        end_directory = filedialog.askdirectory()
        self.ss_directory_label.delete(0, "end")
        self.ss_directory_label.insert(0, end_directory)

    def askDirectory_man(self, event=None):
        global end_directory
        end_directory = filedialog.askdirectory()
        self.man_directory_label.delete(0, "end")
        self.man_directory_label.insert(0, end_directory)
    

# to test this class
def __main__():
    app = tk.Tk()
    tabs = ttk.Notebook(app)
    tabs.grid(row=1, column= 0, sticky="nsew")
    # Create Tabs
    data_input = From_Spreadsheet()
    tabs.add(data_input, text='From Input')
    tk.mainloop()

if __name__ == '__main__':
    __main__()