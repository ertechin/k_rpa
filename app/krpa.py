import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.mouse_controller import MouseController 
from core.keyboard_controller import KeyboardController 
from core.screen_controller import ScreenController
from core.ocr_controller import OcrController
from core.image_controller import ImageController
from core.window_controller import WindowController

class Krpa:
    """ Main entry point for the KRPA framework  """

    def __init__(self):
        self.mouse = MouseController()  # Handles mouse
        self.keyboard = KeyboardController()  # Handles keyboard
        self.screen = ScreenController()  # Handles screen capturing & screenshots 
        self.ocr = OcrController()  # Handles text recognition
        self.image = ImageController()  # Handles image processing
        self.window = WindowController()  # Handles window management

krpa = Krpa()

globals().update({
    "mouse": krpa.mouse,
    "screen": krpa.screen,
    "ocr": krpa.ocr,
    "image": krpa.image,
    "window": krpa.window
})
