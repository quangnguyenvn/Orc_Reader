import argparse
from typing import List
import os

import cv2
import matplotlib.pyplot as plt
from path import Path

import matplotlib.image as img

from image_cutter import detect_words, prepare_img


def get_img_files(data_dir: Path) -> List[Path]:
    """return all image files contained in a folder"""
    res = []
    for ext in ['*.png', '*.jpg', '*.bmp']:
        res += Path(data_dir).files(ext)
    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=Path('../data/line'))
    parser.add_argument('--kernel_size', type=int, default=25)
    parser.add_argument('--sigma', type=int, default=11)
    parser.add_argument('--theta', type=int, default=7)
    parser.add_argument('--min_area', type=int, default=100)
    parser.add_argument('--img_height', type=int, default=50)
    parser.add_argument('--img_name', type=str, default='test')
    parsed = parser.parse_args()
    for fn_img in get_img_files(parsed.data):
        #print(f'Processing file {fn_img}')
        output_filename_path = os.path.splitext(fn_img)[0]
        filename = str(os.path.basename(output_filename_path))
        print(str(filename))
        # load image and process it
        img = prepare_img(cv2.imread(fn_img), parsed.img_height)
        res = detect_words(img,
                       kernel_size=parsed.kernel_size,
                       sigma=parsed.sigma,
                       theta=parsed.theta,
                       min_area=parsed.min_area,
                       basename=filename)
    #plot results
    plt.imshow(img, cmap='gray')
    for det in res:
        xs = [det.bbox.x, det.bbox.x, det.bbox.x +
              det.bbox.w, det.bbox.x + det.bbox.w, det.bbox.x]
        ys = [det.bbox.y, det.bbox.y + det.bbox.h,
              det.bbox.y + det.bbox.h, det.bbox.y, det.bbox.y]
        plt.plot(xs, ys)
    plt.close()


if __name__ == '__main__':
    main()
