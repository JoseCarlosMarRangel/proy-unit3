import cv2
import numpy as np

print(cv2.__version__)

# floodfill with stack and opencv
# https://docs.opencv.org/3.4/d4/d70/tutorial_py_flood_fill.html


class Stack:
    def floodfill(self, img, x, y, label):
        # img: image to be filled
        # x, y: starting point
        # label: label to be filled
        # return: filled image
        h, w = img.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(img, mask, (x, y), label, 0, 0, 255)
        return img


if __name__ == '__main__':
    stack = Stack()
