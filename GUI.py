from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
import os
import PreProccesing as pp
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import ModelCreation as mc

matplotlib.use("TkAgg")


class Root(Tk):
    """
    This class represent our GUI window
    """

    def __init__(self):
        super(Root, self).__init__()
        self.title("K Means Clustering")
        self.minsize(1024, 600)
        self.prep_btn = None
        self.df = None
        self.cluster_btn = None
        self.map_image = None

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
        self.run_num_txt.set_max_val(50)
        self.run_num_txt.set_min_val(1)
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
        self.cluster_num_txt.set_max_val(82)
        self.cluster_num_txt.set_min_val(2)
        self.cluster_num_txt.grid(column=1, row=2, columnspan=2)

    def enable_cluster_button(self):
        if self.run_num_txt.get() and self.cluster_num_txt.get() and self.df is not None:
            self.cluster_btn.config(state="normal")
        else:
            self.cluster_btn.config(state="disabled")

    def create_browse_button(self):
        """
        Create the browse button
        """
        self.button = ttk.Button(self, text="Browse", command=self.file_dialog)
        self.button.grid(column=11, row=1)

    def file_dialog(self):
        """
        This Function opens a filedialog in-order to browse a file in the system
        """
        filename = filedialog.askopenfilename(initialdir="/", title="K Means Clustering", filetype=
        (("Excel Files", "*.xlsx"), ("All Files", "*.*")))
        self.browsed_file_txt.delete(0, len(self.browsed_file_txt.get()))
        self.browsed_file_txt.insert(0, filename)

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
            messagebox.showerror("K Means Clustering", "Please Choose a file first")
        else:
            self.df = pp.load_dataframe(self.browsed_file_txt.get())
            try:
                self.df = pp.pre_process(self.df)
                self.enable_cluster_button()
            except:
                messagebox.showerror("K Means Clustering", "Something went wrong trying to preprocess the file")
                return
            messagebox.showinfo("K Means Clustering", "Preprocessing completed successfully!")

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
            messagebox.showerror("K Means Clustering", "Please insert number of clusters and number of runs")
        else:
            try:
                f = Figure(figsize=(6, 4), dpi=100)
                X, y_kmeans, kmeans = mc.model(self.df, num_of_clusters=int(self.cluster_num_txt.get()),
                                               num_of_run=int(self.run_num_txt.get()))
                scatter_subplot = f.add_subplot(111)
                mc.get_plot(X, y_kmeans, kmeans, scatter_subplot, int(self.cluster_num_txt.get()))

                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().grid(row=7, column=2, columnspan=5)

                dir_of_file = os.path.dirname(self.browsed_file_txt.get())
                path_to_image = mc.choropleth(self.df, dir_of_file)

                map_canvas = Canvas(self, width=550, height=400)
                map_canvas.grid(row=7, column=1)
                self.map_image = PhotoImage(file=path_to_image)

                map_canvas.create_image(-70, -50, anchor=NW, image=self.map_image)

                answer = messagebox.askokcancel("K Means Clustering", "Clustering completed successfully!")
                if answer:
                    self.quit()
            except:
                messagebox.showerror("K Means Clustering", "Something went wrong while trying to do the clustering")

    def quit(self):
        self.destroy()


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
        self.max_val = 11
        self.min_val = 1
        self.get, self.set = self.var.get, self.var.set

    def set_max_val(self, new_max):
        """
        Set the max value to the new_max value
        :param new_max: the max value to be set
        """
        try:
            max_value = int(new_max)
            self.max_val = max_value
        except:
            self.max_val = 11

    def set_min_val(self, new_min):
        """
        Set the min value to the new_min value
        :param new_min: the min value to be set
        """
        try:
            min_value = int(new_min)
            self.min_val = min_value
        except:
            self.max_val = 1

    def check(self, *args):
        """
        Check wether or not the value is a digit and if it is between
        max_value and min_value or if it is an empty String

        if all of the above is true, it sets the value to the new value
        else doesnt change the value
        """
        if self.get().isdigit():
            if self.max_val >= int(self.get()) >= self.min_val:
                # the current value is only digits; allow this
                self.old_value = self.get()
            else:
                self.set(self.old_value)
        elif self.get() == "":
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)

        self.master.enable_cluster_button()
