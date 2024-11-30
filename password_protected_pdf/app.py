from PyPDF2 import PdfWriter, PdfReader
import getpass
#pip install Pypdf2

reader=PdfReader("MLBasicsBook.pdf")
writer=PdfWriter()
#reading pdf using reader and encrypting the pdf
# and then writing using writer

for page in reader.pages:
    writer.add_page(page)

password=getpass.getpass(prompt="Enter the password for the pdf: ")
writer.encrypt(password)
with open('new.pdf', 'wb') as f:
    writer.write(f)