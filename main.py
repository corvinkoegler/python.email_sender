import smtplib
import time
import data
from email.mime.text import MIMEText
from contacts import Contact

# Addressen
contacts = []

with open("mails.txt", "r") as txt:
    for mail in txt:
        contacts.append(Contact("", "", mail))
#contacts.append(Contact("", "", ""))

# Login
gmail_user = data.gmail_user
gmail_password = data.gmail_password

text = """
"""
footer = """


"""

# Senden
for person in contacts:

    # Text
    subject = "Greetings"
    text = f"""
Hallo {person.getVorname()}, 
how are you doing?

{footer}
    """

    msg = MIMEText(text)

    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = person.getMail()

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)

        server.sendmail(gmail_user, msg['To'], msg.as_string())
        server.close()

        print(f'Email send to {person.getMail()}! - Success')
        person.setSend()
        time.sleep(1)
    except:
        print(f'Something went wrong with {person.getMail()}...')

with open("error.txt", "a") as file:
    for person in contacts:
        if not person.getSend():
            file.write(f"{person.getVorname()} {person.getNachname()} {person.getMail()} - Error")