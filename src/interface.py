import tkinter
import tkinter.messagebox
import customtkinter
import easygui

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class Tab(customtkinter.CTk):
    
    def __init__():
        pass

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tabs = []

        # configure window
        self.title("Automatize.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Automatizer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text= "New tab", command=self.add_tab)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text= "Delete tab", command=self.del_tab)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_1)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.tabs = {}
        self.frames = {}

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, rowspan = 3, column=1, columnspan = 3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="New note text")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, text = "Add note", fg_color="black", command = self.new_note)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create tabview


        self.note_cant = 0

    def new_note(self):
        
        actual_tab = self.tabview.get()


        self.note = customtkinter.CTkCheckBox(master = self.tabview.tab(actual_tab), text = self.entry.get(), font = ("Arial", 20), command=self.delete_note)
        self.note.grid(row=self.note_cant, column=0, pady=(20, 20), padx=20, sticky="s")
        self.note_cant += 1
        
    

    
    def add_tab(self):
        
        text = "Enter tab information"
        title = "Tab creation"
        input_list = ["Number", "Name", "Description"]
        number, name, description = easygui.multenterbox(text, title, input_list)
    
        if number not in ("", None): self.tabview.add(f"{number}: {name}") 
        
        # ADD PANDAS
        
    def del_tab(self):
        
        self.note.destroy()
        
    def add_con(self):
        pass
    
    def del_con():
        pass

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()