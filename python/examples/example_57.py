import cv2
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
lmain = tk.Label(root)
lmain.grid()

# Initialize the camera with index 0
cap = cv2.VideoCapture(0)
# You can set the desired resolution here
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


def refresh():
    global imgtk
    ret, frame = cap.read()
    if not ret:
        # Error capturing frame, try next time
        lmain.after(0, refresh)
        return
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    w = lmain.winfo_screenwidth()
    h = lmain.winfo_screenheight()
    cw = cv2image.shape[0]
    ch = cv2image.shape[1]
    # In portrait, image is rotated
    cw, ch = ch, cw
    if (w > h) != (cw > ch):
        # In landscape, we have to rotate it
        cw, ch = ch, cw
        # Note that image can be upside-down, then use clockwise rotation
        cv2image = cv2.rotate(cv2image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # Keep aspect ratio
    w = min(cw * h / ch, w)
    h = min(ch * w / cw, h)
    w, h = int(w), int(h)
    # Get laplacian
    img = cv2.Laplacian(cv2image, cv2.CV_16SC1)
    # Resize to fill the whole screen
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.configure(image=imgtk)
    lmain.update()
    lmain.after(0, refresh)


refresh()
root.mainloop()
