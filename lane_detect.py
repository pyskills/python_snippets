import cv2
import numpy as np

# capturing video through webcam
cap = cv2.VideoCapture(0)

while (1):
    _, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    or_lower = np.array([22, 60, 200], np.uint8)

    or_upper = np.array([60, 255, 255], np.uint8)
    orange = cv2.inRange(hsv, or_lower, or_upper)
    kernal = np.ones((5, 5), "uint8")
    orange = cv2.dilate(orange, kernal)
    res = cv2.bitwise_and(img, img, mask=orange)
    (_, contours, hierarchy) = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            # print(x,y,w,h)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(img, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255))

    cv2.imshow("CV Test", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
