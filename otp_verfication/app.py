import os
import math
import random
import smtplib #SMTP client session object that can be used to send mail to any internet machine with an SMTP
# pip install python-dotenv(for sensitive information)

from dotenv import load_dotenv

#gmail , password
#api keys, sensitive passwords
#2factor enabled - passcode 16 digit code
#smtp protocol: mailing
load_dotenv()
digits="0123456789"
OTP=""
#otp generation
for i in range(6):
    #0-1: 0.5
    #0-9
    #6.5: 6
    OTP+=digits[math.floor(random.random()*10)]
message = OTP+"is your OTP"

smtp_login=smtplib.SMTP('smtp.gmail.com', 587) #server address, post number
smtp_login.starttls()

GMAIL_USER=os.getenv('GMAIL_USER')
GMAIL_PASS=os.getenv('GMAIL_PASS')
#send otp to user
smtp_login.login(GMAIL_USER, GMAIL_PASS)


emailid=input("Enter your mail id: ")
smtp_login.sendmail(GMAIL_USER, emailid, message)

#verify the otp
user_otp = input("Enter your OTP>>: ")
if user_otp == OTP:
    print("OTP entered is correct! User has been verified")
else:
    print("OTP entered is incorrect! User has not been verified")