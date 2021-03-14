from textblob import TextBlob


class Txt_Correction:
    def __init__(self, text):
        self.text = text

    def text_correction(self):
        return TextBlob(self.text)
