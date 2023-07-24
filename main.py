import pyttsx3,PyPDF2

path = open('Video Reflection #5.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(path)

from_page = pdfReader.pages[0]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()