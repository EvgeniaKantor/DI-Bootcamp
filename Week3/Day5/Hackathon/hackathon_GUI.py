import tkinter as tk
from tkinter import ttk
from hackathon_API import generate_CV

class hackathon_GUI:
    root_title = "JOB searcher volunteer"
    #size of the main app window
    screen_ratio_width = 3. / 4
    screen_ratio_height = 3. / 4
    text_initial_CV_width = 30
    text_initial_CV_height = 9

    def __init__(self, root):
        self.modified_cv = ''
        ##########################################
        # Basic parameters of the main window
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
        self.button_CV = tk.Button(self.CV_creator_frame, text="Create CV", command=self.button_CV_command)
        self.button_CV.grid(row=1, column=3, padx=10, pady=10)


        ##########################################
        ##DATABASE frame
        ##########################################
        self.database_frame = tk.Frame(self.root)
        self.database_frame.grid(row=1, column=0, padx=10, pady=10)

        #########################################

        # Creating company name label creation of company tk.Text object
        self.label_company_name = tk.Label(self.database_frame, text="Company name")
        self.label_company_name.grid(row=0, column=0, padx=10, pady=10)
        # Creating company name tk.Text object
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

        ##########################################
        # Creating  Feedback Frame
        ##########################################
        self.feedback_frame = tk.Frame(self.root)
        self.feedback_frame.grid(row=2, column=0, padx=10, pady=10)

        #########################################

        # Creating feedback Label for feedback tk.Text
        self.label_feedback = tk.Label(self.feedback_frame, text="Feedback")
        self.label_feedback.grid(row=0, column=0, padx=10, pady=10)
        # Creating feedback tk.Text object
        self.text_feedback = tk.Text(self.feedback_frame, width=self.text_initial_CV_width,
                                       height=self.text_initial_CV_height)
        self.text_feedback.grid(row=1, column=0, padx=10, pady=10)

        # Creating "Push feedback" button
        self.button_feedback = tk.Button(self.feedback_frame, text="Push feedback")
        self.button_feedback.grid(row=1, column=1, padx=10, pady=10)

        # Creating "Show CV" button
        self.button_show_cv = tk.Button(self.feedback_frame, text="Show CV")
        self.button_show_cv.grid(row=1, column=2, padx=10, pady=10)

        # Creating "Show database" button
        self.button_show_database = tk.Button(self.feedback_frame, text="Show DATABASE")
        self.button_show_database.grid(row=1, column=3, padx=10, pady=10)


    #Definition of Button CV command. It will be bound to button
    def button_CV_command(self):
        # texts extraction from tk.Text widgets
        cv_template_text = self.text_initial_CV.get("1.0", "end-1c")
        job_description = self.text_job_description.get("1.0", "end-1c")
        job_title = self.text_job_title.get("1.0", "end-1c")
        # invoking API function
        self.modified_cv = generate_CV(cv_template_text, job_description, job_title)
        modified_cv_txt = open('modified_cv.txt', "w")
        # Creating txt file
        modified_cv_txt.write(self.modified_cv)
        modified_cv_txt.close()









