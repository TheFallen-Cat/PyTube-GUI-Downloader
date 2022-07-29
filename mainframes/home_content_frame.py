import tkinter as tk
import customtkinter as ctk
import pyperclip as clip

from video_functions import VideoFunctions
from mainframes.video_info_frame import VideoInfoFrame







#============ ContentFrame Window ============

class ContentFrame:


    #============ Init Function ============

    def __init__(self, master, font):

        #============ ContentFrame Window ============

        self.content_frame = ctk.CTkFrame(master)
        self.content_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)
        self.content_frame.grid_columnconfigure(0, weight=1)



        #============ Objects ============

        self.function_manager = VideoFunctions()

        self.video_info_frame = VideoInfoFrame(self.content_frame, font)




        #============ Main Functions ============

        self.search_data_function = lambda : self.function_manager.thread_function(self.video_info_frame.addData, (self.url_entry.get(),))

        self.download_video_function = lambda : self.function_manager.thread_function(self.function_manager.downloadVideo, (self.url_entry.get(), ))



        
        #============ Video Url Frame -> For Entry bar and search button ============

        self.video_url_frame = ctk.CTkFrame(self.content_frame)
        self.video_url_frame.grid(row=0, padx=20, pady=20)


        #============ Url Entry ============

        self.url_entry = ctk.CTkEntry(self.video_url_frame, width=250, placeholder_text="Video Url...", text_font=font)
        self.url_entry.grid(row=0, column=0, padx=5, pady=5)


        #============ Search Button ============

        self.search_video_button = ctk.CTkButton(self.video_url_frame, text="Search", width=50, text_font=font, command=self.search_data_function)
        self.search_video_button.grid(row=0, column=1, padx=5, pady=5)




        #============ Video Info Frame -> For showing all the statistics of the video ============

        self.video_frame = self.video_info_frame



        #============ Download Button ============

        self.search = ctk.CTkButton(self.content_frame, text="Download Now", width=50, text_font=font, command=self.download_video_function)
        self.search.grid(row=3, column=0, padx=5, pady=5)

