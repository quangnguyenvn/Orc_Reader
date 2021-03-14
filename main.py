import logging

import cv2
import pytesseract

from correction import Txt_Correction
from prePossessing import Img_PrePossessing

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

pytesseract.pytesseract.tesseract_cmd = YOUR_CURRENT_TESSERACT_PATH
image_path = YOUR_CURRENT_FILE_PATH

# Step1. Image Pre-Possessing
imgProssessing = Img_PrePossessing(image_path)
img = imgProssessing.prepossessing()
image_text = pytesseract.image_to_string(img)
logger.info('Image/PDF txt:')
logger.info(image_text)

# Step2. Text Correction after reading
textCorrection = Txt_Correction(image_text)
correction_text = textCorrection.text_correction()
logger.info('Text after being corrected:')
logger.info(correction_text)

# Processed Image Review
cv2.imshow('Image', img)
cv2.waitKey(0)
