import win32com.client as win32
import time
from tkinter import Tk


app='word'
wordApp = win32.gencache.EnsureDispatch('%s.Application' %app)
wordApp.Visible = True
myDoc=wordApp.Documents.Add()
myRange = myDoc.Range(0,0)
myRange.InsertBefore('hello python word doc 2 !')
time.sleep(2)
myDoc.SaveAs(r'e:\pydoc.docx')
myDoc.Close()
wordApp.Quit()

