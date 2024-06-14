import math, random
from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_mail(email, token):
    subject = 'your forget password link'
    message = f'hi, click on the link to reset you password https://stockbull-app.onrender.com/change-password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def send_contactus_mail(name,email,title, message):
    subject = f'From Stock Bull---contact us form---'
    message = f' Lead Name: {name} \n\n Lead Email: {email} \n\n Lead Subject: {title} \n\n Lead Message: {message} \n '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mohanmohanraj3778@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return True

def send_OTP(otp, email):
    subject = f'From Stock Bull---Reset-password-form---'
    message = f'OTP: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def generateOTP():
	digits = "0123456789"
	OTP = ""
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]
	return OTP
