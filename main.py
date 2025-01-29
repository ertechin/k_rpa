from app.screen import show_main_screen_and_fps
from app.image_matching  import find_multiple_match, debug_and_check_multiple_image
from app.greetings import say_hello

def main():
    data_set = ['test1.png','test2.png','test3.png','test4.png','test5.png']
    debug_and_check_multiple_image(data_set, 'ms.png')
if __name__ == "__main__":
    main()

