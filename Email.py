import smtplib
from email.message import EmailMessage
import imghdr

sender = 'nahid@gmail.com'
password = ''

massage = EmailMessage()
massage['Subject'] = "i love you nahid."
massage['From'] = sender
massage['To'] = 'nahid23@gmail.com'
massage.set_content('some file ?')
files = ['IMG.jpg','nahid.pdf','n.mp3']
for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    if(file_type == None):
        massage.add_attachment(file_data, maintype='application',
                               subtype='octet-stream', filename=file_name)

    else:
        massage.add_attachment(file_data, maintype='image',
                               subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP('localhost', 1025) as smtp:
# python -m smtpd -c DebuggingServer -n localhost:1025
   # smtp.ehlo()
   # smtp.starttls()
   # smtp.ehlo()
   smtp.login(sender,password)
   smtp.send_message(massage)
