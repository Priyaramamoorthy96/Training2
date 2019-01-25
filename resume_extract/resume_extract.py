import os
from subprocess import Popen, PIPE
from docx import opendocx, getdocumenttext

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

items = os.listdir("/home/priyadharshini/priya/Mytest/resumes")
print (items)
newlist = []
for names in items: 
 print(names)   
 def pdfToTxt(path):
   rsrcmgr = PDFResourceManager()
   retstr = StringIO()
   codec = 'utf-8'
   laparams = LAParams()
   device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
   fp = file(path, 'rb')
   interpreter = PDFPageInterpreter(rsrcmgr, device)
   password = ""
   maxpages = 0
   caching = True
   pagenos=set()
   for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,  password=password,caching=caching, check_extractable=True):
       interpreter.process_page(page)
   fp.close()
   device.close()
   str = retstr.getvalue()
   retstr.close()
   return str

 direc = '/home/priyadharshini/priya/Mytest/resumes'
 direc2 = direc+'/'+names
 val = pdfToTxt(direc2)
 #print(val) 
 t1=names[:-3]
 
 print(names)
 t2='/home/priyadharshini/priya/Mytest/txtfiles/'+t1+'txt'
 filecreate = open(t2,'w') 
 filecreate.write(val)
 print(".txt file created")

