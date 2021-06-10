from textblob import TextBlob

bad_chars = [';', ':', '!', "*", "`", "'"]


class Txt_Correction:
    def __init__(self, text):
        self.text = text

    def text_correction(self):
        self.text = self.removeNonAscii()
        self.text = self.removeBadChars()
        self.text = self.auto_correction()
        return self.text

    def removeNonAscii(self):
        return "".join(i for i in self.text if ord(i) < 128)

    def removeBadChars(self):
        return ''.join((filter(lambda i: i not in bad_chars, self.text)))

    def auto_correction(self):
        return TextBlob(self.text)
