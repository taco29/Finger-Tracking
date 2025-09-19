import cv2
import math

def count_fingers(contour, frame, min_depth=20, max_angle=90):
    """
    Hàm đếm số ngón tay dựa trên convexity defects.
    :param:
     - contour: contour của bàn tay
     - frame: ảnh gốc để vẽ
     - min_depth: độ sâu tối thiểu của defect để tính là khe ngón
     - max_angle: góc tối đa tại defect để tính là khe ngón
    :return:
     - số ngón tay
    """
    hull = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull)
    finger_count = 0

    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])
            depth = d / 256.0

            a = math.dist(end, start)
            b = math.dist(far, start)
            c = math.dist(end, far)
            if b * c == 0:
                continue
            angle = math.acos((b**2 + c**2 - a**2) / (2*b*c)) * 180 / math.pi

            if depth > min_depth and angle < max_angle:
                finger_count += 1
                cv2.circle(frame, far, 5, (255,0,0), -1)

    return finger_count + 1 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không đọc được camera")
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    mask = cv2.inRange(hsv, (0, 130, 77), (255, 180, 127))
    mask = cv2.GaussianBlur(mask, (5,5), 0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    opening = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        continue

    largest_contour = max(contours, key=cv2.contourArea)
    finger_count = count_fingers(largest_contour, frame)

    cv2.drawContours(frame, [largest_contour], -1, (0,255,0), 2)
    hull_points = cv2.convexHull(largest_contour)
    cv2.drawContours(frame, [hull_points], -1, (0,0,255), 2)

    cv2.putText(frame, f"Fingers: {finger_count}", (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
