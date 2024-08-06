import tkinter
import tkinter.messagebox
import customtkinter
import easygui
import numpy

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tabs = []

        # configure window
        self.title("Automatize.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # ----------------------SIDEBAR--------------------------
        # SIDEBAR FRAMES
        self.sidebar = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        # SIDEBAR WIDGETS
        self.logo_label = customtkinter.CTkLabel(self.sidebar, text="Automatizer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.outputs_button = customtkinter.CTkButton(self.sidebar, text= "Outputs", command=lambda:self.show_frame("Outputs"))
        self.outputs_button.grid(row=1, column=0, padx=20, pady=10)
        self.inputs_button = customtkinter.CTkButton(self.sidebar, text= "Inputs", command=lambda:self.show_frame("Inputs"))
        self.inputs_button.grid(row=2, column=0, padx=20, pady=10)
        self.config_button = customtkinter.CTkButton(self.sidebar, text= "Settings", command=lambda:self.show_frame("Settings"))
        self.config_button.grid(row=3, column=0, padx=20, pady=10)
        # --------------------------------------------------------
        
        # ---------------------CONTAINER--------------------------
        # CONTAINER FRAME
        container = customtkinter.CTkFrame(self, corner_radius=0, fg_color = "blue")
        container.grid(row=0, column=1, rowspan=4, sticky="nsew")
        # CONTAINER FUNCTIONALITY
        self.frames = {}
        for F in (Inputs, Outputs, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("Outputs")
        # --------------------------------------------------------
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()    

class Outputs(customtkinter.CTkFrame):
    
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="red")
        self.controller = controller
        
        
        #self.tabview = customtkinter.CTkTabview(self, width=750)
        #self.tabview.grid(row=0, rowspan = 3, column=0, columnspan = 3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        #self.tabview = customtkinter.CTkTabview(self)
        #self.tabview.grid(row=0, rowspan = 3, column=1, columnspan = 3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create main entry and button
        #self.entry = customtkinter.CTkEntry(self, placeholder_text="New note text")
        #self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        #self.main_button_1 = customtkinter.CTkButton(master=self, text = "Add note", fg_color="black")
        #self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
         
        #self.new_tab_button = customtkinter.CTkButton(self, text= "New tab", command=self.add_tab)
        #self.new_tab_button.grid(row=4, column=0, padx=20, pady=10)        
        
    def add_tab(self):
        
        text = "Enter tab information"
        title = "Tab creation"
        input_list = ["Number", "Name", "Description"]
        number, name, description = easygui.multenterbox(text, title, input_list) 
        if number not in ("", None): self.tabview.add(f"{number}: {name}") 
        # ADD PANDAS
        

class Inputs(customtkinter.CTkFrame):
    
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
class Settings(customtkinter.CTkFrame):
    
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller        
        
        
        """
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


        # create main entry and button
        
        self.new_tab_button = customtkinter.CTkButton(self, text= "New tab", command=self.add_tab)
        self.new_tab_button.grid(row=3, column=1, padx=20, pady=10)
        # create tabview


        self.note_cant = 0
        """
    # SIDEBAR BUTTONS FUNCTIONS
    
    def show_output(self):
        pass
    
    def show_input(self):
        pass
    
    def show_config(self):
        pass
    
    
    
    def new_note(self):
        
        actual_tab = self.tabview.get()
        self.note = customtkinter.CTkCheckBox(master = self.tabview.tab(actual_tab), text = self.entry.get(), font = ("Arial", 20), command=self.delete_note)
        self.note.grid(row=self.note_cant, column=0, pady=(20, 20), padx=20, sticky="s")
        self.note_cant += 1


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