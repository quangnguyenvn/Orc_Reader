import glob
from PIL import Image
import sys
import os

folder = "Images"

param_1 = sys.argv[1]
param_2 = sys.argv[2]
os.mkdir(param_1)

if __name__ == '__main__':
    images = glob.glob(folder+"\\*.jpg")
    for image in images:
        img = Image.open(image)
        img_name = str(img.filename)
        img.save(param_1 + "\\" + img_name[7:len(img_name)], quality=int(param_2))
        print('process: ' + str(img_name[7:len(img_name)]))
        
print('finish')