import win32com.client as win32
import time
from tkinter import Tk


app='excel'
xlApp = win32.gencache.EnsureDispatch('%s.Application' %app)
xlApp.Visible = True
xlBook = xlApp.Workbooks.Add()
xlApp.Worksheets.Add().Name = 'test'
shSheet = xlApp.Worksheets('test')

shSheet.Cells(1,1).Value='python-to-%s Demo' %app
time.sleep(1)
for i in range(3,8):
    shSheet.Cells(i,1).Value='Line %d ' % i
    time.sleep(1)
shSheet.Cells(i+2,1).Value = "Th-th-th-that's all folks!"
time.sleep(4)
xlBook.SaveAs(r'e:\excel.xlsx')
xlBook.Close(False)

xlApp.Application.Quit()