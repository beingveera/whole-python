from PIL import Image
import numpy as np
import cv2
import curses

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
scale = 0.15
scale_x = 1.75

scr = curses.initscr()
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            # Error capturing frame, try next time
            continue
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = Image.fromarray(frame)
        S = (round(img.size[0] * scale * scale_x), round(img.size[1] * scale))
        img = np.asarray(img.resize(S))
        img = (img / 255.) * (chars.size - 1)
        for i, r in enumerate(chars[img.astype(int)]):
            try:
                scr.addstr(i, 0, "".join(r))
            except KeyboardInterrupt:
                raise
            except:
                pass
        scr.refresh()
except KeyboardInterrupt:
    scr.endwin()
    raise
