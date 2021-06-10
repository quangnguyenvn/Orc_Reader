import logging
import os
import sys

import cv2
import pytesseract

from correction import Txt_Correction
from pdfReader import pdf_Read
from prePossessing import Img_PrePossessing

pytesseract.pytesseract.tesseract_cmd = {YOUR_CURRENT_TESSERACT_EXE_PATH}
# EXP: pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# log output file from 3rd param when run cmd
logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_handler = logging.FileHandler(str(sys.argv[2]))
# set level of log - DEBUG - WARNING - ERROR - Can catch in verbose argv cmd
c_handler.setLevel(logging.DEBUG)
# set logger format
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

# get file path from 2nd param when run cmd
file_path = str(sys.argv[1])

# Check file types for each case: images or pdf
split_path = os.path.splitext(file_path)
file_extension = split_path[1]

if file_extension == '.png' or file_extension == '.jpeg' or file_extension == '.jpg':
    # Step1. Image Pre-Possessing
    imgProssessing = Img_PrePossessing(file_path)
    img = imgProssessing.prepossessing()
    image_text = pytesseract.image_to_string(img)
    logger.warning('Image txt:')
    logger.warning(image_text)

    # Step2. Remove unrecognized char and text Correction after reading
    textCorrection = Txt_Correction(image_text)
    correction_text = textCorrection.text_correction()
    logger.warning('Text after being corrected:')
    logger.warning(correction_text)

    # Processed Image Review
    cv2.imshow('Image', img)
    cv2.waitKey(0)

elif file_extension == '.pdf':
    # Step.1 Extract text from pdf file
    pdf_read = pdf_Read(file_path)
    pdf_text = pdf_read.text_reading()

    # Step.2 Correction pdf text after reading
    textCorrection = Txt_Correction(pdf_text)
    correction_text = textCorrection.text_correction()
    logger.warning('PDF reading text:')
    logger.warning(correction_text)

else:
    logger.warning('Can not determine file type: ' + str(split_path))
