import tkinter as tk
from hackathon_GUI import hackathon_GUI
from hackathon_GUI_gpt_design import StyledHackathonGUI


if __name__ == '__main__':
    root = tk.Tk()

#    window_hackathon_GUI = hackathon_GUI(root)
    window_hackathon_GUI = StyledHackathonGUI(root)

    root.mainloop()