import cv2
import numpy as np

def nothing(x):
    pass

def draw_shape(event, x, y, flags, param):
    global drawing, shape, ix, iy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img[:] = np.zeros((400, 600, 3), np.uint8)
            draw_shapes()
            if shape == 'circle':
                cv2.circle(img, (ix, iy), abs(x - ix), color, -1)
            elif shape == 'rectangle':
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            elif shape == 'ellipse':
                cv2.ellipse(img, (ix, iy), (abs(x - ix), abs(y - iy)), 0, 0, 360, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if shape == 'circle':
            cv2.circle(img, (ix, iy), abs(x - ix), color, -1)
        elif shape == 'rectangle':
            cv2.rectangle(img, (ix, iy), (x, y), color, -1)
        elif shape == 'ellipse':
            cv2.ellipse(img, (ix, iy), (abs(x - ix), abs(y - iy)), 0, 0, 360, color, -1)

def draw_shapes():
    cv2.putText(img, "Press C for Circle, R for Rectangle, E for Ellipse", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.namedWindow("Shapes")
cv2.setMouseCallback("Shapes", draw_shape)

cv2.createTrackbar("R", "Shapes", 0, 255, nothing)
cv2.createTrackbar("G", "Shapes", 0, 255, nothing)
cv2.createTrackbar("B", "Shapes", 0, 255, nothing)

drawing = False
ix, iy = -1, -1
shape = 'circle'
img = np.zeros((400, 600, 3), np.uint8)

draw_shapes()

while True:
    r = cv2.getTrackbarPos("R", "Shapes")
    g = cv2.getTrackbarPos("G", "Shapes")
    b = cv2.getTrackbarPos("B", "Shapes")
    color = (b, g, r)
    
    cv2.imshow("Shapes", img)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('c'):
        shape = 'circle'
    elif key == ord('r'):
        shape = 'rectangle'
    elif key == ord('e'):
        shape = 'ellipse'

cv2.destroyAllWindows()
