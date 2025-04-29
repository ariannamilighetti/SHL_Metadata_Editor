import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Metadata_Changes(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.instructions_label = 0
        self.table_titles_rows = 1
        self.search_button_row = 2
        self.list_row = 4

        self.instructions = tk.Label(master=self, text='Use this tab to add an entry to the data validation in the metadata crator. \nUse the search bar to search the collections list.', anchor="w", justify='left')
        self.instructions.grid(column=0, row=0, columnspan=3, sticky='nw')
        var = tk.IntVar()
        update = tk.Radiobutton(self, text="Update validation", variable=var, value=1, command=self.update_command)
        update.grid(column=0,row=1)
        add = tk.Radiobutton(self, text="Add validation Entry", variable=var, value=2, command=self.add_command)
        add.grid(column=0,row=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
    
    def get_file(self, list_option):
        if list_option == "Collections List":
            file = 'collections_validation.txt'
        elif list_option == "Digitiser List":
            file = 'digitiser_validation.txt'
        elif list_option == "Access List":
            file = 'access_validation.txt'
        elif list_option == "Copyright List":
            file = 'copyright_validation.txt'
        elif list_option == "Restrictions List":
            file = 'restriction_validation.txt'
        else:
            file = 'empty.txt'
        
        return file

    def show_current_list(self, eventObject):
        list_option = eventObject.widget.get()  
        file = self.get_file(list_option) 
        data = self.list_box_contents(file)
        self.fill_listbox(data, current_list)
        return file 
        
    def get_selection(self):
        global selected_item
        index = current_list.curselection()
        selected_item = current_list.get(index)
        update_value_entry.delete(0, 'end')
        update_value_entry.insert(0, selected_item)

    def show_options(self):
        options_label = tk.Label(self, text="Select the validation set to update")
        options_label.grid(column=0, row = 3)
        choose_validation= tk.StringVar()
        options = ("Collections List", "Digitiser List", "Access List", "Copyright List", "Restrictions List")
        global drop_menu
        drop_menu= ttk.Combobox(self, textvariable=choose_validation)
        drop_menu['values']= options
        drop_menu['state']= 'readonly'
        drop_menu.grid(column=0, row=4, sticky='n')
        drop_menu.bind("<<ComboboxSelected>>", self.show_current_list)  
        global current_list
        current_list = tk.Listbox(self, width=60, height=5,selectmode=tk.SINGLE)
        current_list.grid(column=1, row=4, columnspan=2, sticky='ew')
        
    def update_command(self):
        self.show_options()
        global update_value_entry
        update_value_label = tk.Label(self, text="Value to update")
        update_value_entry = tk.Entry(self, width = 60)
        get_selection_button = tk.Button(self,text="Get from box", width=25, command=self.get_selection, bg = '#ea7847', fg='#f5f3f1')    
        update_value_label.grid(column=0, row=5, sticky='e')
        update_value_entry.grid(column=1, row=5)
        get_selection_button.grid(column = 2, row = 5, sticky= 'ew', padx=5, pady=5)
        value_updated_label = tk.Label(self, text="Enter updated value")
        value_updated_entry = tk.Entry(self, width = 60)
        value_updated_button = tk.Button(self,text="Confirm",width=25,command=lambda: self.update_file(update_value_entry.get(), value_updated_entry.get()))  
        value_updated_label.grid(column=0, row=6, sticky='e')
        value_updated_entry.grid(column=1, row=6, columnspan=2, sticky='ew')
        value_updated_button.grid(column=1, row=7, sticky= 'ew', padx=5, pady=5)
    
    def add_command(self):
        self.show_options()
        update_value_label = tk.Label(self, text="Value to add")
        update_value_entry = tk.Entry(self, width = 60)
        get_selection_button = tk.Button(self,text="Confirm",width=25, command=lambda:self.add_value(update_value_entry.get()))
        update_value_label.grid(column=0, row=5, sticky='e')
        update_value_entry.grid(column=1, row=5)
        get_selection_button.grid(column = 2, row = 5, sticky= 'ew', padx=5, pady=5)

    def add_value(self, added_value):
        label = "Value added"
        already_existing = False
        selected_entry = drop_menu.get()
        file = self.get_file(selected_entry)
        filedata = []
        file_r = open(file, 'r')
        added_value = added_value + '\n'
        for entry in file_r:
            filedata.append(entry)
            if entry.lower() == added_value.lower():
                already_existing = True
                label = "Value already in validation"
        
        if already_existing == False:
            filedata.append(added_value)
            filedata.sort()

            file_w = open(file, 'w')
            
            for i in filedata:
                file_w.write(i)
            file_w.close()

        success_label = tk.Label(self, text=label)
        success_label.grid(column=2, row=7)


    def update_file(self, old, new):
        selected_entry = drop_menu.get()
        file = self.get_file(selected_entry)
        filedata = []
        file_r = open(file, 'r')
        for x, entry in enumerate(file_r):
            filedata.append(entry)
            if entry.replace("\n",'') == old:
                filedata[x] = (new + '\n')
            
            
        file_w = open(file, 'w')
        
        for i in filedata:
            file_w.write(i)
        file_w.close()
        success_label = tk.Label(self, text="Validation Updated")
        success_label.grid(column=2, row=7)
    
    def cb_search(self, event):
        sstr = self.search_str.get()
        self.Lb.delete(0, 'end')

        # If filter removed show all data
        if sstr == "":
            self.fill_listbox(self.coll_data, self.Lb)
            return
    
        filtered_data = list()
        for item in self.coll_data:
            if item.lower().find(sstr.lower())>= 0:
                filtered_data.append(item)
    
        self.fill_listbox(filtered_data, self.Lb)   

    def fill_listbox(self, item_list, lb):
        lb.delete(0,'end')
        for item in item_list:
            lb.insert('end', item)

    def list_box_contents(self, file):
        data = []
        f = open(file,"r")
        for x in f:
            data.append(x)
        f.close()
        return data


# to test this class
def __main__():
    app = tk.Tk()
    tabs = ttk.Notebook(app)
    tabs.grid(row=1, column= 0, sticky="nsew")
    # Create Tabs
    data_input = Metadata_Changes()
    tabs.add(data_input, text='From Input')
    tk.mainloop()

if __name__ == '__main__':
    __main__()