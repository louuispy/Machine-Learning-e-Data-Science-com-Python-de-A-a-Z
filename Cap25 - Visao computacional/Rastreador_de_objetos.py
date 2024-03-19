import cv2
print(cv2.__version__)

rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('rua.mp4')
ok, frame = video.read()

bbox = cv2.selectROI(frame)
# print(bbox)

ok = rastreador.init(frame, bbox)
# print(ok)

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox
