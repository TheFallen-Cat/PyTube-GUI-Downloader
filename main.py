#External Imports
import customtkinter as ctk
import os
from PIL import Image, ImageTk
from mainframes.setting_frame import SettingsFrame


#Inbuilt Imports
from mainframes.video_info_frame import VideoInfoFrame
from mainframes.options_frame import OptionFrame
from mainframes.home_content_frame import ContentFrame





class MainApp:

    def __init__(self):

        #============ Main Window ============

        self.root = ctk.CTk()
        self.root.geometry("700x400")

        
        #============ Main Window Configurations ============

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.main_font = ('Segoe UI Black', 10)
        

        #============ Options Frame ============

        self.option_frame = OptionFrame(self.root, self.main_font)



        #============ Content/Results Frame ============

        self.content_frame = ContentFrame(self.root, self.main_font)

        self.settings_frame = SettingsFrame(self.root)



        self.root.mainloop()




app = MainApp()