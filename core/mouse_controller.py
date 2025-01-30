from pynput.mouse import Controller as Mouse, Button

class MouseController:
    def __init__(self):
        """ Initialize mouse controller. """
        self.mouse = Mouse()

    def move_to(self, x, y):
        """ Move mouse to an absolute position. """
        self.mouse.position = (x, y)
    
    def left_click(self):
        """ Simulate mouse left click. """
        self.mouse.click(Button.left)

    def right_click(self):
        """ Simulate mouse right click. """
        self.mouse.click(Button.right)

    def scroll(self, dx, dy):
        """ Scroll the mouse wheel. """
        self.mouse.scroll(dx, dy)
