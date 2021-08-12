import smtplib
from email.message import EmailMessage
import imghdr
import getpass


def main():
    print("\t\t-------------------------LogIn Gmail---------------------------\n")
    sender = input("\t\tEnter Your Gmail Address: ")
    password = getpass.getpass("\t\tEnter Your Password: ")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(sender, password)
            massage = EmailMessage()
            massage['From'] = sender
            massage['To'] = input("\t\tTo: ")
            massage['Subject'] = input("\t\tSubject: ")
            body = input("\t\tBody: ")
            massage.set_content(body)

            print("\t\tDo you want to add files(Y/N)?", end="")
            y=input()
            if(y=='Y' or y=='y'):
                c = True
                files = []
                while(c):
                    url = input("\t\tEnter File URL: ")
                    files.append(url)
                    print("\t\tDo you want to add more files(Y/N)?", end="")
                    x = input()
                    if(x == 'N'or x=='n'):
                        c = False

                for file in files:
                    with open(file, "rb") as f:
                        if f != None:
                            file_data = f.read()
                            file_type = imghdr.what(f.name)
                            file_name = f.name
                            if(file_type == None):
                                massage.add_attachment(file_data, maintype='application',
                                                    subtype='octet-stream', filename=file_name)

                            else:
                                massage.add_attachment(file_data, maintype='image',
                                                    subtype=file_type, filename=file_name)
            try:
                smtp.send_message(massage)
                print("\n\t\tEmail has been successfully delivered.")
            except smtplib.SMTPSenderRefused:
                print("\n\t\tEmail is not delivered!")
                                                    
        except smtplib.SMTPAuthenticationError:
            print("\n\t\tYour email and password are wrong!")


if __name__ == '__main__':
    main()
