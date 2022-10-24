from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib, os, datetime, pickle

def read_from_bin(pos):
    # 0 - export path
    # 1 - mail id
    # 2 - password
    # 3 - saved host
    # 4 - saved user
    # 5 - saved password
    # 6 - saved database
    # 7 - temp host
    # 8 - temp user
    # 9 - temp password
    # 10 - temp database
    file = open("cache.bin", 'rb+')
    foobar=pickle.load(file)
    data = str(foobar[pos])
    file.close()
    return data

def read_mail_creds():
    mail_id=read_from_bin(1)
    password=read_from_bin(2)
    return mail_id,password

def write_to_bin(func, path, mail_id, password):
    file = open("cache.bin", 'rb+')
    if func==0: # write mail creds
        path=read_from_bin(0)
        content=[path, mail_id, password]
        pickle.dump(content, file)
    elif func==1: # write path
        mail_id,password=read_mail_creds()
        content=[path, mail_id, password]
        pickle.dump(content, file)
    file.close()

def send_mail(dbs_creds,table):
    mail_id, password=read_mail_creds()
    currenttime = str(datetime.date.today())
    out_path=currenttime+" exported_dbs.csv"

    currenttime = datetime.datetime.now()
    # current_time = currenttime.strftime("%H%M%S")
    sender_email = "mail-id"
    receiver_email = "mail-id"
    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = receiver_email
    message['Subject'] = str(currenttime)
    
    attachment_Path = os.path.join(out_path) # add date to name for fail safe

    try:
        with open(attachment_Path, "rb") as attachment:
            p = MIMEApplication(attachment.read(),_subtype="csv")	
            p.add_header('Content-Disposition', "attachment; filename="+out_path) 
            message.attach(p)

    except Exception as l:
        pass

    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(mail_id, password)
    email_session.sendmail(sender_email, mail_id, my_message)
    email_session.quit()

if __name__ == "__main__":
    # print(read_mail_creds())
    print("foobar")