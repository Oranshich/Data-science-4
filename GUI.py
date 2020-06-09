from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import PreProccesing as pp


class Root(Tk):
    """
    This class represent our GUI window
    """

    def __init__(self):
        super(Root, self).__init__()
        self.title("Data Science HW 4")
        self.minsize(1024, 600)
        self.prep_btn = None
        self.df = None
        self.cluster_btn = None

        # Create the layouts
        self.create_browse_titles()

        self.create_clusters_options()

        self.create_runs_options()

        self.create_browse_button()

        self.create_preprocess_button()
        self.create_cluster_button()

    def create_browse_titles(self):
        """
        Create the browse title
        :return:
        """
        self.browse_lbl = Label(self, text="Open File:")
        self.browse_lbl.grid(column=0, row=1, pady=10)
        self.browsed_file_txt = Entry(self, width=100)
        self.browsed_file_txt.grid(column=1, row=1, columnspan=9, padx=5)

    def create_runs_options(self):
        """
        Create the number of runs option,
        both the label and the entry,
        Only accepts numbers
        """
        self.run_num_lbl = Label(self, text="Number of runs:")
        self.run_num_lbl.grid(column=0, row=3, pady=10)
        self.run_num_txt = NumberEntry(self, width=25)
        self.run_num_txt.grid(column=1, row=3, columnspan=2)

    def create_clusters_options(self):
        """
        Create the number of clusters option,
        both the label and the entry,
        Only accepts numbers
        """
        self.cluster_num_lbl = Label(self, text="Number of clusters k:")
        self.cluster_num_lbl.grid(column=0, row=2, pady=10)
        self.cluster_num_txt = NumberEntry(self, width=25)
        self.cluster_num_txt.grid(column=1, row=2, columnspan=2)

    def create_browse_button(self):
        """
        Create the browse button
        """
        self.button = ttk.Button(self, text="Browse A File", command=self.file_dialog)
        self.button.grid(column=11, row=1)

    def file_dialog(self):
        """
        This Function opens a filedialog in-order to browse a file in the system
        """
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("Excel Files", "*.xlsx"), ("All Files", "*.*")))
        self.browsed_file_txt.delete(0, len(self.browsed_file_txt.get()))
        self.browsed_file_txt.insert(0, filename)
    #
    # def get_browsed_path(self):
    #     return self.browsed_file_txt.get()
    #
    # def get_cluster_num(self):
    #     return self.cluster_num_txt.get()
    #
    # def get_run_num(self):
    #     return self.run_num_txt.get()

    def create_preprocess_button(self):
        """
        Create the Preprocess button in the grid layout
        """
        self.prep_btn = ttk.Button(self, text="Pre-process", command=self.preprocess)
        self.prep_btn.grid(column=1, row=5, columnspan=3)

    def preprocess(self):
        """
        This function is applying the preprocess stage,
        first it validates that the user already chose a file,
        then loads the file into a pandas Dataframe,
        then tries to preprocess it according to the HW instructions
        if something is not as excpected it will display an error message box
        else it displays a info message box the the preprocess is completed
        """
        if not self.browsed_file_txt.get():
            messagebox.showerror("File Path is missing", "Please Choose a file first")
        else:
            self.df = pp.load_dataframe(self.browsed_file_txt.get())
            try:
                self.df = pp.pre_process(self.df)
            except:
                messagebox.showerror("Error", "Something went wrong trying to preprocess the file")
                return
            self.cluster_btn.config(state="normal")
            messagebox.showinfo("Pre-Process Done", "Preprocessing completed successfully!")

    def create_cluster_button(self):
        """
        Create the Preprocess button in the grid layout
        """
        self.cluster_btn = ttk.Button(self, text="Cluster", command=self.kmeans_data)
        self.cluster_btn.grid(column=1, row=6, columnspan=3)
        self.cluster_btn.config(state="disabled")

    def kmeans_data(self):
        """
        This function is calculating the kmeans but the cluster number and number of runs,
        first it check if the user already preproccessed the dataframe,
        then checks if the user inserted numbers in the input values
        and then starting the kmean function as in the instructions
        """
        if (not self.cluster_num_txt.get()) or (not self.run_num_txt.get()):
            messagebox.showerror("Missing values", "Please insert number of clusters and number of runs")
        else:
            print(self.df)


class NumberEntry(Entry):
    """
    This class extends the Entry class of Tkinter
    which represents the input
    this class only accepts numbers and empty strings
    """
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        super(NumberEntry, self).__init__(master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit():
            if(int(self.get()) <= 11 and int(self.get()) > 0):
                # the current value is only digits; allow this
                self.old_value = self.get()
            else:
                self.set(self.old_value)
        elif  self.get() == "":
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)
