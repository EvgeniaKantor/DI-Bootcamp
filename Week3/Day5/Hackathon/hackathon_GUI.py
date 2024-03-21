import tkinter as tk
from tkinter import ttk

class hackathon_GUI:
    root_title = "JOB searcher volunteer"
    #size of the main app window
    screen_ratio_width = 3. / 4
    screen_ratio_height = 3. / 4
    text_initial_CV_width = 30
    text_initial_CV_height = 5

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
        self.CV_creator_frame.grid(row=0, column=0, padx=10, pady=10)

        #########################################

        # initial CV label creation of CV tk.Text object
        self.label_initial_CV = tk.Label(self.CV_creator_frame, text="Text of your initial CV")
        self.label_initial_CV.grid(row=0, column=0, padx=10, pady=10)
        # initial CV tk.Text object
        self.text_initial_CV = tk.Text(self.CV_creator_frame, width=self.text_initial_CV_width,
                                       height=self.text_initial_CV_height)
        self.text_initial_CV.grid(row=1, column=0, padx=10, pady=10)
        # Creating job title Label
        self.label_job_title = tk.Label(self.CV_creator_frame, text="Job Title")
        self.label_job_title.grid(row=0, column=1, padx=10, pady=10)
        # Creating job title tk.Text object
        self.text_job_title = tk.Text(self.CV_creator_frame, width=self.text_initial_CV_width,
                                      height=self.text_initial_CV_height)
        self.text_job_title.grid(row=1, column=1, padx=10, pady=10)
        #Creating job description Label
        self.label_job_description = tk.Label(self.CV_creator_frame, text="Job Description")
        self.label_job_description.grid(row=0, column=2, padx=10, pady=10)
        # Creating job description tk.Text object
        self.text_job_description = tk.Text(self.CV_creator_frame, width=self.text_initial_CV_width,
                                            height=self.text_initial_CV_height)
        self.text_job_description.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        # Creating CV creation Button
        self.button_CV = tk.Button(self.CV_creator_frame, text="Create CV")
        self.button_CV.grid(row=1, column=3, padx=10, pady=10)


        ##########################################
        ##DATABASE frame
        ##########################################
        self.database_frame = tk.Frame(self.root)
        self.database_frame.grid(row=1, column=0, padx=10, pady=10)

        #########################################
        # company name label creation of company tk.Text object
        self.label_company_name = tk.Label(self.database_frame, text="Company name")
        self.label_company_name.grid(row=0, column=0, padx=10, pady=10)
        # company name tk.Text object
        self.text_company_name= tk.Text(self.database_frame, width=self.text_initial_CV_width,
                                       height=self.text_initial_CV_height)
        self.text_company_name.grid(row=1, column=0, padx=10, pady=10)
        # Creating company address Label
        self.label_company_address = tk.Label(self.database_frame, text="Company address")
        self.label_company_address.grid(row=0, column=1, padx=10, pady=10)
        # Creating  Company address tk.Text object
        self.text_company_address = tk.Text(self.database_frame, width=self.text_initial_CV_width,
                                      height=self.text_initial_CV_height)
        self.text_company_address.grid(row=1, column=1, padx=10, pady=10)
        #Creating Contact Person Label
        self.label_contact_person = tk.Label(self.database_frame, text="Contact Person")
        self.label_contact_person.grid(row=0, column=2, padx=10, pady=10)
        # Creating Contact Person tk.Text object
        self.text_contact_person = tk.Text(self.database_frame, width=self.text_initial_CV_width,
                                            height=self.text_initial_CV_height)
        self.text_contact_person.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        # Creating "Submit to database button"
        self.button_database = tk.Button(self.database_frame, text="Submit to Database")
        self.button_database.grid(row=1, column=3, padx=10, pady=10)
#








