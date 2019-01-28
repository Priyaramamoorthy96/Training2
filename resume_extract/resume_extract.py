import os
import re
import xlwt 
from xlwt import Workbook 
from subprocess import Popen, PIPE
from docx import opendocx, getdocumenttext
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def document_to_text(filename, file_path):
    if filename[-4:] == ".doc":
        cmd = ['antiword', file_path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')

    elif filename[-5:] == ".docx":
        document = opendocx(file_path)
        paratextlist = getdocumenttext(document)
        newparatextlist = []
        for paratext in paratextlist:
            newparatextlist.append(paratext.encode("utf-8"))
        return '\n\n'.join(newparatextlist)
    elif filename[-4:] == ".odt":
        cmd = ['odt2txt', file_path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')
    elif filename[-4:] == ".pdf":
        return pdfToTxt(direc2)
   
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
items = os.listdir("/home/priyadharshini/priya/mycodes/resume_extract/resumes/")
print (items)
newlist = []
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 
i=1
sheet1.write(0, 0, "Filename")
sheet1.write(0, 1, "MailId")
sheet1.write(0, 2, "PhoneNumber")
sheet1.write(0, 3, "languages_Count")
for names in items: 
 print(names)
 direc = '/home/priyadharshini/priya/mycodes/resume_extract/resumes/'
 direc2 = direc+names
 val = document_to_text(names,direc2)
 #print(val)
 mail = re.findall('\S+@\S+', val)
 phone = re.findall(r'\d{10}', val) 
 print(mail)
 print(phone)
 t1=names[:-3] 
 t3=t1+'txt'
 t2='/home/priyadharshini/priya/mycodes/resume_extract/txtfiles/'+t3
 filecreate = open(t2,'w') 
 filecreate.write(val)
 print(".txt file created")
 filecreate.close()
 n=0
 j=4
 #print(mail)
 infile2 = open("/home/priyadharshini/priya/mycodes/resume_extract/languages.txt","r") 
 for line1 in infile2:
   for word1 in line1.split():  
     #print(word1)
     f=1
     infile1 = open(t2,"r")
     for line2 in infile1:
       for word2 in line2.split():
         word2=word2.lower()
         word2=re.sub('[,|.|/|!]', '', word2)
         #print(word2)
         #print("====")
         if word1==word2:
           if f==1:
             n=n+1
             sheet1.write(i, j, word1) 
             j=j+1
             f=0
     infile1.close()   
 print(n)
 sheet1.write(i, 0, names)  
 sheet1.write(i, 1, mail)
 sheet1.write(i, 2, phone)
 sheet1.write(i, 3, n)


 n=0
 i=i+1
 j=4
 wb.save('/home/priyadharshini/priya/mycodes/resume_extract/resume_info.xls') 



