import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.input_controller import InputController
from core.screen_controller import ScreenController 
from core.ocr_controller import OcrController 
from core.image_controller import ImageController 

class Krpa(InputController, ScreenController, OcrController, ImageController):
    def __init__(self):
        InputController.__init__(self)
        ScreenController.__init__(self)
        OcrController.__init__(self)
        ImageController.__init__(self)

