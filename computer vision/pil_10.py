from PIL import Image
import glob, os
size = 128, 128
for infile in glob.glob(r"C:\\Users\\techno\\Desktop\\calc.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".jpg", "JPEG")
