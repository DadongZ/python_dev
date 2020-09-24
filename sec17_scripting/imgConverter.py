import os
import sys
from PIL import Image

if len(sys.argv) != 3:
    print('imgConverter requires two arguments')

dirin = sys.argv[1]
dirout = sys.argv[2]

if not os.path.exists(dirout):
    print(f"creating new dir {dirout}")
    os.makedirs(dirout)

for i in os.listdir(dirin):
    img = Image.open(os.path.join(dirin, i))
    imgid = os.path.splitext(i)[0]+'.png'
    img.save(os.path.join(dirout, imgid), 'png')

    