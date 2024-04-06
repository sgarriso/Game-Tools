from tkinter import *
from tkinter import ttk

class tkDriver:
    def __init__(self,  *args, **kwargs):
        self.root  = Tk(*args, **kwargs)
        self.create_frame()
        
    def create_frame(self,*args, **kwargs):
        self.frame = ttk.Frame(self.root, *args, **kwargs)
        self.frame.grid()
    
    def create_label(self, *args, **kwargs):
        grid = kwargs.pop("grid", {})
        ttk.Label(self.frame, *args, **kwargs).grid(**grid)
    
    def create_quit_button(self):
        
        self.create_button(text="Quit", command=self.root.destroy,  grid={"column": 1, "row": 0})
    def create_button(self,*args, **kwargs):
         grid = kwargs.pop("grid", {})
         ttk.Button(self.frame, *args, **kwargs).grid(**grid)
    
        
        
        
    
    def run_loop(self, *args, **kwargs):
        self.root.mainloop()
    
    def create_basic_app(self):
        self.create_frame(padding=10)
        self.create_label(text="Hello World!", grid={"column": 0, "row": 0})
        self.create_quit_button()
        self.run_loop()
    
