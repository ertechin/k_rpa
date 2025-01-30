from pynput.keyboard import Controller as Keyboard, Key

class KeyboardController:
    
    def __init__(self):
        """ Initialize keyboard controller. """
        self.keyboard = Keyboard()

    def press_key(self, key):
        """ Press and release a key (e.g., 'a', 'enter')."""
        if len(key) == 1:
            self.keboard.press(key)
            self.keboard.release(key)
        else:
            self.keyboard.press(getattr(Key, key, key))
            self.keyboard.release(getattr(Key, key, key))

    def type_text(self, text):
        """ Type a full string like human typing. """
        self.keyboard.type(text)
