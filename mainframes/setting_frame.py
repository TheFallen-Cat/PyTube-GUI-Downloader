import tkinter as tk
import customtkinter as ctk


class SettingsFrame:


    #============ Initialization ============
    def __init__(self, master = None, font = ('Segoe UI Black', 10)):

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)
        self.main_frame.grid_forget()



        self.lab = ctk.CTkLabel(self.main_frame, text="This is still in development!", text_font=font)
        self.lab.pack()



    #============ Attributes/Functions ============

    #showFrame Function -> To show the frame by unforgetting the grid

    def showFrame(self):
        self.main_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)


    #hideFrame Function -> ofc, the vide versa of showFrame function

    def hideFrame(self):
        self.main_frame.grid_forget()






