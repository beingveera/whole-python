import sys
import tkinter
import urllib

from PIL import Image, ImageDraw, ImageFont, ImageTk

import torch
from torchvision import transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn

COCO_INSTANCE_CATEGORY_NAMES = ['__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
# URL of the image that will be processed
IMAGE_URL = "https://github.com/pytorch/hub/raw/master/dog.jpg"
MIN_SCORE = 0.5


# We don't have a terminal available in GUI mode, so let's simulate it
class stdredir(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.widget = tkinter.Text(self.root)
        self.widget.pack(fill='both', expand=True)
        self.text = ''

    def write(self, string):
        self.text += string.replace('\b', '')
        if '\r' in string:
            cutto = self.text.rindex('\r')
            sfrom = -1
            try:
                sfrom = self.text.rindex('\n', 0, cutto)
            except:
                pass
            self.text = self.text[:sfrom + 1] + self.text[cutto + 1:]

    def flush(self):
        self.widget.delete(1.0, tkinter.END)
        self.widget.insert(tkinter.END, self.text)
        self.widget.see(tkinter.END)
        self.widget.update()


redir = stdredir()
sys.stdout = redir
sys.stderr = redir

print('Downloading image...')
url, filename = (IMAGE_URL, "image.jpg")
urllib.request.urlretrieve(url, filename)

print('Loading model...')
sys.stdout.flush()

model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

print('Detecting objects, please wait...')
sys.stdout.flush()

image = Image.open(filename)
# This model doesn't require resize
preprocess = transforms.Compose([
    transforms.ToTensor(),
])
input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)
with torch.no_grad():
    output = model(input_batch)
classes = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in list(output[0]['labels'].numpy())]
boxes = [[(i[0], i[1]), (i[2], i[3])] for i in list(output[0]['boxes'].detach().numpy())]
scores = list(output[0]['scores'].detach().numpy())

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 72)
for clss, box, score in zip(classes, boxes, scores):
    if score > MIN_SCORE:
        draw.rectangle(box, width=3)
        draw.text(box[0], clss, font=font)

# Close the text window
sys.stdout.root.destroy()

# Show the result
root = tkinter.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
lmain = tkinter.Label(root)
lmain.grid()
imgtk = ImageTk.PhotoImage(image=image)
lmain.configure(image=imgtk)
lmain.update()
root.mainloop()
