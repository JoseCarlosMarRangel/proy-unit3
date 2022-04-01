
import cv2
import matplotlib.pyplot as plt
import numpy as np

print("Version del opencv: ")
print(cv2.__version__, "\n")


# * Clase stack para tener un stack manual
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# * Obtener y poner pixel
def getpixel(img, x, y):
    return img[x, y]

# * Pone los pixeles con el label recibido de de la funcion floodfill


def putpixel(x, y, label):
    # Poner pixeles en la imagen usando el stack
    img[x, y] = label

    return img


# * Se obtiene el label de las regiones
def region_labeling(th1):
    m = 2
    # print(th1.shape)
    for i in range(th1.shape[0]):
        for j in range(th1.shape[1]):
            #print(th1[i, j])
            if th1[i, j] == 255:
                floodfill(th1, i, j, m)
                m = m + 1
    return th1


# * Se hace el floodfill
def floodfill(img, x, y, label):
    stack = Stack()
    stack.push((x, y))
    while not stack.isEmpty():
        stack.pop()
        height, width = img.shape[:2]

        if((x >= 0) and (x < width) and (y >= 0)
           and (y < height) and getpixel(img, x, y) == 1):
            print("Entro en flood fill")
            #print("height: ", height, "width: ", width)
            #putpixel(x, y, label)
            putpixel(x, y, label)

            stack.push((x + 1, y))
            stack.push((x, y + 1))
            stack.push((x, y - 1))
            stack.push((x - 1, y))


# * Metodo main
if __name__ == '__main__':
    #img = cv2.imread('00-puppy.jpg', 0)
    img = cv2.imread('floodfill3.png', 0)
    original = cv2.imread('floodfill3.png')
    original = cv2.resize(original, (400, 400))
    cv2.imshow('Original', original)
    img = cv2.resize(img, (400, 400))
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("SimpleBinarizacion", th1)
    # cv2.waitKey()
    #img2 = region_labeling(th1)
    #cv2.imshow("Imagen labeling", img2)
    img3 = putpixel(0, 0, 255)
    cv2.imshow("resultado final", img3)
    cv2.waitKey()
