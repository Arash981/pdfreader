import pyttsx3
import PyPDF2
from tkinter.filedialog import *

#taking file name
book = askopenfilename()

#inisilise it with pdf reader it is an object
pdfreader = PyPDF2.PdfFileReader(book)

#get the number of pages from pdf file
pages = pdfreader.getNumPages

#read all the data from the pdf page 
for num in range (0, pages):
    page = pdfreader.getPage(num)
    # extract the text from pdf
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()



