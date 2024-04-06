from drivers.UIdriver.UIdriver import UIDriver




class Storyboard:
    def __init__(self):
        self.ui_driver = UIDriver()
    def create_app(self):
        self.ui_driver.create_basic_app()
    