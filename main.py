import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

# capture screen
wincap = WindowCapture()

# initialize characters and items
character_img = cv.imread('images/red.jpg', cv2.IMREAD_GRAYSCALE)
character_shape = cv.Canny(character_img, 100, 200)

# red_character = Vision('images/red.jpg')
# orange_character = Vision('images/orange.jpg')
# pink_character = Vision('images/pink.jpg')
# cyan_character = Vision('images/cyan.jpg')
# blue_character = Vision('images/blue.jpg')
# purple_character = Vision('images/purple.jpg')
# green_character = Vision('images/green.jpg')
# lime_character = Vision('images/lime.jpg')
# black_character = Vision('images/black.jpg')
# white_character = Vision('images/white.jpg')
# yellow_character = Vision('images/yellow.jpg')
# brown_character = Vision('images/brown.jpg')


# detect characters and items in the map
loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    # red_rectangles = red_character.find(screenshot, 0.5)

    # output_image = red_character.draw_rectangles(screenshot, red_rectangles)
    # output_image = orange_character.draw_rectangles(output_image, orange_rectangles)
    # output_image = pink_character.draw_rectangles(output_image, _rectangles)
    # output_image = cyan_character.draw_rectangles(output_image, cyan_rectangles)
    # output_image = blue_character.draw_rectangles(output_image, blue_rectangles)
    # output_image = purple_character.draw_rectangles(output_image, purple_rectangles)
    # output_image = green_character.draw_rectangles(output_image, green_rectangles)
    # output_image = lime_character.draw_rectangles(output_image, lime_rectangles)
    # output_image = black_character.draw_rectangles(output_image, black_rectangles)
    # output_image = white_character.draw_rectangles(output_image, white_rectangles)
    # output_image = yellow_character.draw_rectangles(output_image, yellow_rectangles)
    # output_image = brown_character.draw_rectangles(output_image, brown_rectangles)

    cv.imshow('Matches', screenshot)

    print('FPS {}'.format(1/ (time()-loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
