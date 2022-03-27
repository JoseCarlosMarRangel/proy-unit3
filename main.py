import cv2
from cv2 import floodFill
import numpy as np

print(cv2.__version__)

# floodfill with stack and opencv
# https://docs.opencv.org/3.4/d4/d70/tutorial_py_flood_fill.html


# Stack needed for floodfill
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Floodfill function


def getpixel(img, x, y):
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            print(img[x, y])


def putpixel(x, y, label):


def floodfill(img, x, y, label):
    stack = Stack()
    stack.push((x, y))
    while not stack.isEmpty():
        stack.pop()
        # obtener largo y ancho de la imagen
        height, width = img.shape[:2]
        print("height: ", height, "width: ", width)
        if((x >= 0) and (x < width) and (y >= 0)
           and (y < height) and getpixel(img, x,
                                         y) == 1):
            putpixel(x, y, label)

            stack.push((x + 1, y))
            stack.push((x, y + 1))
            stack.push((x, y - 1))
            stack.push((x - 1, y))

    return img


if __name__ == '__main__':
    img = cv2.imread('floodfill3.png')
    cv2.imshow('image original', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # getpixel()
    floodfill(img, 10, 10, 50)
    cv2.imwrite('resultado.png', floodfill(img, 10, 10, 50))
