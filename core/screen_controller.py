import mss
import mss.tools
import os
import time
from datetime import datetime
import cv2 as cv
import numpy as np

SAVE_DIR = "screenshots"
os.makedirs(SAVE_DIR, exist_ok = True)

def time_stamped_filename(prefix="screenshot", extension=".png"):
    """ create a uniq filename for screen shots """

    time_stamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
    return f"{prefix}_{time_stamp}{extension}"

def take_screenshot(file_name="screenshot.jpg"):
    """ take full screenshot of first screen under screenshots folder """

    location_and_name = os.path.join(SAVE_DIR, file_name)
        
    with mss.mss() as  sct:
        sct.shot(output = location_and_name)
        print(f"screenshot saved as {location_and_name}")

def take_training_shots():
    print ("starting the taking screenshot every 240 S")
    try:
        while True:
            take_screenshot(time_stamped_filename("training_shot"))
            time.sleep(240)
    except KeyboardInterrupt:
        print ("screenshot taking stoped")

def take_screenshot_by_coordinates(x, y, width, height, file_name="region_shot", extension=".png"):
    """ take a screenshot of a specific region defined by coordinates """

    location_and_name = os.path.join(SAVE_DIR, file_name)
    
    region = {"top": y, "left": x, "width": width, "height": height}
    
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=location_and_name)
        print(f"Region screenshot saved as {location_and_name}")

def get_screen_size():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        width = monitor["width"]
        height = monitor["height"]
    return width, height

class ScreenController:
    def capture_screen(self):
        """Live screen capturing with FPS display."""
        w, h = get_screen_size()
        print("mss Screen Capture Speed Test")
        print(f"Screen Resolution: {w}x{h}")

        t0 = time.time()
        n_frames = 0 
        monitor = {"top": 0, "left": 0, "width": w, "height": h}

        with mss.mss() as sct:
            try:
                while True:
                    img = sct.grab(monitor)
                    img = np.array(img)

                    small = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

                    cv.imshow("k_rpa", small)

                    elapsed_time = time.time() - t0
                    n_frames += 1
                    avg_fps = n_frames / elapsed_time
                    print(f"\rAverage FPS: {avg_fps:.2f}", end="")

                    key = cv.waitKey(1) & 0xFF
                    if key == ord('q'): 
                        print("\nExiting...")
                        break
            except KeyboardInterrupt:
                print("\nInterrupted by user (Ctrl+C)")
            finally:
                cv.destroyAllWindows()

