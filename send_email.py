from email.message import EmailMessage
import smtplib
import ssl



emailSender= "1messigogo510@gmail.com"
passwordSender = "colx neyh lffp vfpm"


emailReciever ="hadob84454@twugg.com"

subject = "Congratulations!!"
body = "we would find you well \n and we want to tell you that you have been selected to be in our community \n congratulations again"

em =EmailMessage()
em['from'] = emailSender
em['to'] = emailReciever
em['subject'] = subject
em.set_content(body)


context =ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com' , 465 ,context=context) as smtp :
    smtp.login(emailSender ,passwordSender)
    smtp.sendmail(emailSender,emailReciever,em.as_string())
