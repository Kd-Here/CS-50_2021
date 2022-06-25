MY_ADDRESS = "waitingforyou9899@gmail.com"         # Replace with yours
MY_PASSWORD = "qflhewmbvikuyjhj"      # Replace with yours
RECIPIENT_ADDRESS = "wipaj96845@syswift.com, qknohrluhknjnazkci@kvhrs.com"  # Replace with yours

HOST_ADDRESS = 'smtp.gmail.com'   # Replace with yours
HOST_PORT = 587               


# this is smtp lib 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)

# Create a mime multipart object
oas = MIMEMultipart()


# Setting up our object
oas['From'] = MY_ADDRESS
oas['To'] = RECIPIENT_ADDRESS
oas['Subject'] = "Checking Python Automation Mail features."

# Creating a The content for email which is mimetext part
content_Automated_Mail = MIMEText("This is Automated mail from Kds welcome to our group! Thanks for been a part of this family",'plain')


oas.attach(content_Automated_Mail)

# Send Email and close connection
server.send_message(oas)
server.quit()

# Just to debug
print("Mail is send!")