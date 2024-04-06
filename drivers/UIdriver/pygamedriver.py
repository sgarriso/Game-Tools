import pygame
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.tuple = (self.red, self.green, self.blue)
class pygameDriver:
    WHITE = Color(255,255,255) # or 'white'
    RED = Color(255,0,0)
    def __init__(self,  *args, **kwargs):
        self.root = pygame.init()
        self.mapping = {}
        
        self.running = True
    def create_frame(self, *args, **kwargs):
        self.frame = pygame.display.set_mode( *args, **kwargs)
    def set_background(self, color:Color):
        self.background = color.tuple
        self.frame.fill(self.background)
    def create_label(self, *args, **kwargs):
        grid = kwargs.pop("grid", {})
        text = self.font.render(*kwargs["label"])
        self.mapping[text] = {"rect":text.get_rect(**grid), "quit":kwargs.get("quit", False) }
    def set_font(self, *args, **kwargs):
        self.font = pygame.font.SysFont(*args, **kwargs)
    
    def run_loop(self, *args, **kwargs):
        while self.running:
            for event in pygame.event.get():
                for item in self.mapping:
                    if event.type == pygame.QUIT:
                        self.running = False
                        break
                    self.frame.blit(item, self.mapping[item]["rect"])
                    pygame.draw.rect(self.frame, pygameDriver.RED.tuple, self.mapping[item]["rect"], 1 )
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.mapping:
                        if self.mapping[item]["rect"].collidepoint(event.pos) and self.mapping[item]["quit"]:
                            self.running = False
            pygame.display.update()
    def create_basic_app(self):
        self.create_frame((400,300))
        self.set_font("Arial", 14)
        self.create_label(label=("Hello World!", True, self.WHITE.tuple), grid={"topleft":(10,10)})
        self.create_label(label=("Quit!", True, self.WHITE.tuple), grid={"topleft":(100,10)},quit=True)
        self.set_background(Color(127,127,127))
        self.run_loop()
                
                    
                   
           
        