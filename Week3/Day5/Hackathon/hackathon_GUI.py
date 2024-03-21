import tkinter as tk
from tkinter import ttk

class hackathon_GUI:
    root_title = "JOB searcher volunteer"
    #size of the main app window
    screen_ratio_width = 3. / 4
    screen_ratio_height = 3. / 4
    text_initial_CV_width = 20

    def __init__(self, root):
        ##########################################
        ##Basic parameters of the main window
        ##########################################
        self.root = root
        self.root.title(self.root_title)
        # request of screen parameters
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        # creating of main window size parameters
        self.root_width = int(self.screen_width * self.screen_ratio_width)
        self.root_height = int(self.screen_height * self.screen_ratio_height)
        # creating of positioning parameters of the main window
        self.root_center_x = int(self.screen_width / 2 - self.root_width / 2)
        self.root_center_y = int(self.screen_height / 2 - self.root_height / 2)
        # assigning the screen parameters to members of main window
        self.root.geometry(f"{self.root_width}x{self.root_height}+{self.root_center_x}+{self.root_center_y}")
        # dividing root into 3 parts for CV creator Frame, DATABASE Frame and Feedback Frame
        self.root.grid_rowconfigure(0, weight=1, uniform='row')
        self.root.grid_rowconfigure(1, weight=1, uniform='row')
        self.root.grid_rowconfigure(2, weight=1, uniform='row')
        ##########################################
        ##CV creator Frame
        ##########################################
        self.CV_creator_frame = tk.Frame(self.root)
        self.CV_creator_frame.grid(row=0, column=0, padx=10, pady=10, rowspan=1)
        # initial CV label creation of CV tk.Text object
        self.label_initial_CV = tk.Label(self.CV_creator_frame, text="Text of your initial CV")
        self.label_initial_CV.grid(row=0, column=0, padx=10, pady=10)
        # initial CV tk.Text object
        self.text_initial_CV = tk.Text(self.CV_creator_frame, width=self.text_initial_CV_width)
        self.text_initial_CV.grid(row=1, column=0, padx=10, pady=10)







