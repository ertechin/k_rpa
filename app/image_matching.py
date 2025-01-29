import cv2 as cv
import numpy as np
import time

def random_loc(x, y, w, h):
    # TODO :: 
    return (1,2,3,4)

def center_loc(x, y, w, h):
    center_x = x + int(w/2)
    center_y = x + int(h/2)
    return center_x, center_y

def method_white(haystack, needle, threshold):
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    locations = np.where(result >=  threshold)
    return locations 

def method_black(haystack, needle, threshold):
    result = cv.matchTemplate(haystack, needle, cv.TM_SQDIFF_NORMED)
    locations = np.where(result <= threshold)
    return locations 

def find_single_match():
    # TODO :: 
    return (1,2,3,4)


def find_multiple_match(haystack_img_path, needle_img_path, threshold=0.9, method='white', r_loc='center', debug_mode=None):
    # Read the images
    haystack = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    needle = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
    # Find needle image h and w
    needle_w = needle.shape[1]
    needle_h = needle.shape[0]
    # Define wich method wil bee use
    locations = method_white(haystack, needle, threshold) if method == 'white' else method_black(haystack, needle, threshold)
    # Reverse locations
    locations = list(zip(*locations[::-1]))
    # Create rectangle [x, y, w, h] list
    rectangles = []
    for loc in locations:
            rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
            # add two times for rectangle group
            rectangles.append(rect) # TODO :: look best practice
            rectangles.append(rect)
    # Group the closest rectangles
    rectangles, weights = cv.groupRectangles(rectangles,1,0.4)
    points = []
    if len(rectangles):
        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = line_color 
        marker_type = cv.MARKER_CROSS
        # Loop over all the locations and draw their rectangle
        for (x, y, w, h) in rectangles:
            # Find the return loc
            r_loc_x, r_loc_y = center_loc(x,y,w,h) if r_loc == 'center' else random_loc(x,y,w,h)
            # Add to the points
            points.append( (r_loc_x, r_loc_y) )
            if debug_mode == 'rectangles':
                # Determine the box positions
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Draw the rectangle
                cv.rectangle(haystack, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                # Draw X
                cv.drawMarker(haystack, center_loc(x,y,w,h), marker_color, marker_type)
        if debug_mode:
            cv.imshow('MATCHES' , haystack)
            cv.waitKey()
    return points

def debug_and_check_multiple_image(haystacks, needle, method = 'multiple', cv_func='white'):
    for img in haystacks:
        # TODO :: add single match
        find_multiple_match(img, needle, debug_mode='rectangles')
        cv.destroyAllWindows()

