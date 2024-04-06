from drivers.UIdriver.tkdriver import tkDriver
from drivers.UIdriver.pygamedriver import pygameDriver
from drivers.UIdriver.pygamedriver import Color
class UIDriver:
    def __init__(self, driver=True):
        print(driver)
        self.client = tkDriver() if driver else  pygameDriver()
    
    def create_frame(self, *args, **kwargs):
        self.client.create_frame(*args, **kwargs)
    
    def create_label(self, *args, **kwargs):
        self.client.create_label(*args, **kwargs)
    
    def create_quit_button(self, *args, **kwargs):
        self.client.create_quit_button(*args, **kwargs)
    def set_font(self, *args, **kwargs):
        self.client.set_font(*args, **kwargs)
    def run_loop(self,  *args, **kwargs):
        self.client.run_loop(*args, **kwargs)
    def set_background(self, *args, **kwargs):
        self.client.set_background(*args, **kwargs)
    
    def create_basic_app_pygame(self):
        self.create_frame((400,300))
        self.set_font("Arial", 14)
        self.create_label(label=("Hello World!", True, pygameDriver.WHITE.tuple), grid={"topleft":(10,10)})
        self.create_label(label=("Quit!", True, pygameDriver.WHITE.tuple), grid={"topleft":(100,10)},quit=True)
        self.set_background(Color(127,127,127))
        self.run_loop()
    def create_basic_app(self):
        self.client.create_basic_app()
    
    def create_text_event_editor_app(self):
        pass
        
        
        
        