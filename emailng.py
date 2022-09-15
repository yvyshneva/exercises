from email.message import EmailMessage

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)

print(message)
# From: me@example.com
# To: you@example.com
# Subject: Greetings from me@example.com to you@example.com!
# MIME-Version: 1.0
# Content-Type: text/plain; charset="utf-8"
# Content-Transfer-Encoding: 7bit
# 
# Hey there!
# 
# I'm learning to send email using Python!

#########################
import os.path
import mimetypes

attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
# image/png

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
# image
print(mime_subtype)
# png

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

print(message)
"""
Content-Type: multipart/mixed; boundary="===============5350123048127315795=="

--===============5350123048127315795==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hey there!

I'm learning to send email using Python!

--===============5350123048127315795==
Content-Type: image/png
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="example.png"
MIME-Version: 1.0

iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
(...We deleted a bunch of lines here...)
wgAAAABJRU5ErkJggg==

--===============5350123048127315795==--
"""

###############
import smtplib

# mail_server = smtplib.SMTP('localhost') -> gives an ConnectionRefusedError
mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1)

#################
import getpass
mail_pass = getpass.getpass('Password? ')
# Password?

mail_server.login(sender, mail_pass)
# (235, b'2.7.0 Accepted')

mail_server.send_message(message)
mail_server.quit()
