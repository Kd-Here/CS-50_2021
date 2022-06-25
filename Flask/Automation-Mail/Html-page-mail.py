MY_ADDRESS = "waitingforyou9899@gmail.com"         # Replace with yours
MY_PASSWORD = "qflhewmbvikuyjhj"      # Replace with yours
RECIPIENT_ADDRESS = "fgp61673@zcrcd.com, sudsdezzzzcxzfvjvd@kvhrw.com"  # Replace with yours

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
# Since sending html page instead of plain it's should be alternative

oas = MIMEMultipart('alternative')


# Setting up our object
oas['From'] = MY_ADDRESS
oas['To'] = RECIPIENT_ADDRESS
oas['Subject'] = "Checking Python Automation Mail features."

# Creating a The content for email which is mimetext part




html_Content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        span{
            background-color: brown;
            color: bisque;
        }
        h1{
            color: rgb(66, 100, 129);
        }
        h2{
            font-style: italic;
        }
    </style>
</head>
<body>
    <span>
        <h1>THIS IS great to see you</h1>
        <a href="https://www.youtube.com/"></a>
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/32/Bugatti_Centodieci_side.png" width="700px" height="60px" alt="">
        <h2>We are Thanking you to be part of Kd's </h2>
    </span>
</body>
</html> """

HTML=MIMEText(html_Content,'html')

oas.attach(HTML)
# Send Email and close connection
server.send_message(oas)
server.quit()

# Just to debug
print("Mail is send!")