from core.keyboard_controller import KeyboardController
from core.mouse_controller import MouseController

class InputController(KeyboardController, MouseController):
    """Unified input controller that combines keyboard and mouse functionality."""

    def __init__(self):
        """ Initialize keyboard and mouse controllers. """
        KeyboardController.__init__(self)
        MouseController.__init__(self)
