from hackathon_GUI import hackathon_GUI
class StyledHackathonGUI(hackathon_GUI):
    def __init__(self, root):
        super().__init__(root)
        self.apply_styles()

    def apply_styles(self):
        # Define custom fonts and colors
        default_font = ('Helvetica', 10)
        title_font = ('Helvetica', 14, 'bold')
        background_color = '#ffffcc'  # Light yellow
        text_color = '#333333'
        button_color = '#800080'  # Purple
        button_text_color = 'white'

        # Apply styles to CV creator frame
        self.CV_creator_frame.config(bg=background_color)
        self.label_initial_CV.config(font=title_font, fg=text_color)
        self.text_initial_CV.config(font=default_font)
        self.label_job_title.config(font=title_font, fg=text_color)
        self.text_job_title.config(font=default_font)
        self.label_job_description.config(font=title_font, fg=text_color)
        self.text_job_description.config(font=default_font)
        self.button_CV.config(font=default_font, bg=button_color, fg=button_text_color)

        # Apply styles to Database frame
        self.database_frame.config(bg=background_color)
        self.label_company_name.config(font=title_font, fg=text_color)
        self.text_company_name.config(font=default_font)
        self.label_company_address.config(font=title_font, fg=text_color)
        self.text_company_address.config(font=default_font)
        self.label_contact_person.config(font=title_font, fg=text_color)
        self.text_contact_person.config(font=default_font)
        self.button_database.config(font=default_font, bg=button_color, fg=button_text_color)

        # Apply styles to Feedback frame
        self.feedback_frame.config(bg=background_color)
        self.label_feedback.config(font=title_font, fg=text_color)
        self.text_feedback.config(font=default_font)
        self.button_feedback.config(font=default_font, bg=button_color, fg=button_text_color)
        self.button_show_cv.config(font=default_font, bg=button_color, fg=button_text_color)
        self.button_show_database.config(font=default_font, bg=button_color, fg=button_text_color)
        self.root.configure(bg='#ffffcc')
        self.root.maxsize(int(self.root_width), int(self.root_height))
        self.root.minsize(int(self.root_width), int(self.root_height))

