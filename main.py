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
    #print("entro en putpixel")
    return img


# * Se obtiene el label de las regiones
def region_labeling(th1):
    m = 0
    # print(th1.shape)
    for i in range(th1.shape[0]):
        for j in range(th1.shape[1]):
            #print(th1[i, j])
            if th1[i, j] == 255:
                #print("entro para floodfill")
                floodfill(th1, i, j, m)
                m = m + 1
    # regresar imagen labeleada
    return th1


# * Se hace el floodfill
def floodfill(img, x, y, label):
    stack = Stack()
    stack.push((x, y))
    while not stack.isEmpty():
        stack.pop()
        height, width = img.shape[:2]
        if((x >= 0) and (x < width) and (y >= 0)
           and (y < height) and getpixel(img, x, y) <= 1):
            putpixel(x, y, label)

            stack.push((x + 1, y))
            stack.push((x, y + 1))
            stack.push((x, y - 1))
            stack.push((x - 1, y))

    img2 = putpixel(x, y, label)
    cv2.imshow("img2", img2)


# * Metodo main
if __name__ == '__main__':
    img = cv2.imread('floodfill3.png', 0)
    img = cv2.resize(img, (400, 400))
    ret, th1 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
    cv2.imshow("SimpleBinarizacion", th1)
    region_labeling(th1)
    cv2.waitKey()
