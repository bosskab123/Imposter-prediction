import numpy as np
import cv2 as cv

class Vision:

    object_img = None
    object_w = 0
    object_h = 0
    method = None

    def __init__(self, object_img_path, method = cv.TM_CCOEFF_NORMED):
        self.object_img = cv.imread(object_img_path, cv.IMREAD_UNCHANGED)
        self.object_w = self.object_img.shape[1]
        self.object_h = self.object_img.shape[0]
        self.method = method

    def find(self, bg_img, threshold = 0.5):
        result = cv.matchTemplate(bg_img, self.object_img, self.method)
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        if not locations:
            return np.array([], dtype = np.int32).reshape(0,4)

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.object_w, self.object_h]
            rectangles.append(rect)
            rectangles.append(rect)
        
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold = 1, eps=0.5)
        return rectangles
    
    def get_click_points(self, rectangles):
        points = []
        for (x,y,w,h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            points.append((center_x,center_y))
        return points
    
    def draw_rectangles(self, bg_img, rectangles):
        line_color = (0,255,0)
        line_type = cv.LINE_4
        for (x,y,w,h) in rectangles:
            top_left = (x,y)
            bottom_right = (x+w,y+h)
            cv.rectangle(bg_img, top_left, bottom_right, line_color, lineType = line_type)
        return bg_img
    
    def draw_crosshair(self, bg_img, points):
        marker_color = (255,0,255)
        marker_type = cv.MARKER_CROSS
        for (center_x,center_y) in points:
            cv.drawMarker(bg_img, (center_x,center_y), marker_color, marker_type)
        return bg_img
    