



# TO DOWHLOAD EMAIL ATTACHMENT 
from operator import add
import os
from email import message
import imaplib
import email
from imapclient.imap_utf7 import decode

user=input("enter your email")
password=input("enter the password")
imap_url="imap.gmail.com"
attachment_directory=r"Enter directory you want to save the attachment"

con=imaplib.IMAP4_SSL(imap_url)
con.login(user,password)
con.select("INBOX")


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

def search():
    result,data=(con.search(None,'FROM','"Enter email to be filtered"'))
    return data

def get_emails(result_bytes):
    msgs=[]
    for num in result_bytes[0].split():
        type,data= con.fetch(num,'(RFC822)')
        msgs.append(data)
    return msgs

def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=="multitype":
            continue
        if part.get('Content-Disposition') is None:
            continue
        filename=part.get_filename()
        if bool(filename):
            filePath=os.path.join(attachment_directory,filename)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))       
    
x=search()
print(x)
result,data=con.fetch(b'100','(RFC822)')
raw=email.message_from_bytes(data[0][1])
get_attachments(raw)




