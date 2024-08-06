import random as rd
import tkinter 
import config as st
from tkinter import font as ctfont


import customtkinter as ct



class SampleApp(ct.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        

        self.geometry("200x200")
        self.resizable(0, 0)

        container = ct.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Create, Folders, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(ct.CTkFrame):
    
    def __init__(self, parent, controller):

        ct.CTkFrame.__init__(self, parent)
        self.controller = controller
        ct.CTkLabel(self, text="POST IT!", height=50).grid(row=0, sticky="NSEW")
        ct.CTkButton(self, text = "Create", command=lambda: controller.show_frame("Create"), height=50).grid(row=1, sticky="NSEW")
        ct.CTkButton(self, text = "Folders", command=lambda: controller.show_frame("Folders"), height=50).grid(row=2, sticky="NSEW")
        ct.CTkButton(self, text = "Settings", command=lambda: controller.show_frame("Settings"), height=50).grid(row=3, sticky="NSEW")

class Create(ct.CTkFrame):
    
    def __init__(self, parent, controller):
        ct.CTkFrame.__init__(self, parent)
        self.controller = controller

class Folders(ct.CTkFrame):
    def __init__(self, parent, controller):
        ct.CTkFrame.__init__(self, parent) 
        self.controller = controller

class Settings(ct.CTkFrame):
    def __init__(self, parent, controller):
        ct.CTkFrame.__init__(self, parent)
        self.controller = controller



if __name__ == "__main__":
    
    settings = st.Settings()
    app = SampleApp()
    app.mainloop()
