import logging
import os

import cv2
import pytesseract

from correction import Txt_Correction
from pdfReader import pdf_Read
from prePossessing import Img_PrePossessing

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

# initializing bad_chars_list for removing from reading text
bad_chars = [';', ':', '!', "*", "`", "'"]

pytesseract.pytesseract.tesseract_cmd = YOUR_CURRENT_TESSERACT_EXE_PATH
file_path = YOUR_CURRENT_FILE_PATH

# remove nonAscii char from txt method
def _removeNonAscii(text):
    return "".join(i for i in text if ord(i) < 128)


# Check file types for each case: images or pdf

split_path = os.path.splitext(file_path)
file_extension = split_path[1]

if file_extension == '.png' or file_extension == '.jpeg' or file_extension == '.jpg':
    # Step1. Image Pre-Possessing
    imgProssessing = Img_PrePossessing(file_path)
    img = imgProssessing.prepossessing()
    image_text = pytesseract.image_to_string(img)
    logger.info('Image txt:')
    logger.info(image_text)

    # Step2. Remove unrecognized char and text Correction after reading
    nonAscii_txt = _removeNonAscii(str(image_text))
    refined_txt = ''.join((filter(lambda i: i not in bad_chars, str(nonAscii_txt))))
    textCorrection = Txt_Correction(refined_txt)
    correction_text = textCorrection.text_correction()
    logger.info('Text after being corrected:')
    logger.info(correction_text)

    # Processed Image Review
    cv2.imshow('Image', img)
    cv2.waitKey(0)

elif file_extension == '.pdf':
    # Step.1 Extract text from pdf file
    pdf_read = pdf_Read(file_path)
    pdf_text = pdf_read.text_reading()

    # Step.2 Correction pdf text after reading
    nonAscii_txt = _removeNonAscii(str(pdf_text))
    refined_txt = ''.join((filter(lambda i: i not in bad_chars, str(nonAscii_txt))))
    textCorrection = Txt_Correction(refined_txt)
    correction_text = textCorrection.text_correction()
    logger.info('PDF reading text:')
    logger.info(correction_text)

else:
    logger.info('Can not determine file type.')
