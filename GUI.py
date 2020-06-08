from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Root(Tk):


    def __init__(self):
        super(Root, self).__init__()
        self.title("Data Science HW 4")
        self.minsize(1024, 600)

        self.create_browse_titles()

        self.create_clusters_options()
        self.create_runs_options()

        self.create_browse_button()

    def create_browse_titles(self):
        self.browse_lbl = Label(self, text="Open File:")
        self.browse_lbl.grid(column=0, row=1, pady=10)
        self.browsed_file_txt = Entry(self, width=100)
        self.browsed_file_txt.grid(column=1, row=1, columnspan=9, padx=5)

    def create_runs_options(self):
        self.run_num_lbl = Label(self, text="Number of runs:")
        self.run_num_lbl.grid(column=0, row=3, pady=10)
        self.run_num_txt = number_entry(self, width=25)
        self.run_num_txt.grid(column=1, row=3, columnspan=2)

    def create_clusters_options(self):
        self.cluster_num_lbl = Label(self, text="Number of clusters k:")
        self.cluster_num_lbl.grid(column=0, row=2, pady=10)
        self.cluster_num_txt = number_entry(self,width=25)
        self.cluster_num_txt.grid(column=1, row=2, columnspan=2)

    def create_browse_button(self):
        self.button = ttk.Button(self, text="Browse A File", command=self.fileDialog)
        self.button.grid(column=11, row=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("Excel Files", "*.xlsx"), ("All Files", "*.*")))
        self.browsed_file_txt.delete(0, len(self.browsed_file_txt.get()))
        self.browsed_file_txt.insert(0, self.filename)

    def get_browsed_path(self):
        return self.browsed_file_txt.get()

    def get_cluster_num(self):
        return self.cluster_num_txt.get()

    def get_run_num(self):
        return self.run_num_txt.get()



class number_entry(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        super(number_entry,self).__init__(master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit() or self.get() == "":
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)
