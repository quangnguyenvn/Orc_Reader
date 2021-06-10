import PyPDF2


class pdf_Read:
    def __init__(self, file_path):
        self.file_path = file_path

    def text_reading(self):
        pdf_file = open(self.file_path, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        return page_content.encode('utf-8')
