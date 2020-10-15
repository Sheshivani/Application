import smtplib



sender_email = input("email_id: ")
rec_email = "XXXX@gmail.com"
password = input("password: ")
msg = "hello python send mail"

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(sender_email, password)
print("login sucessfully")
server.sendmail(sender_email,rec_email,msg)
print("email send successfully!!",rec_email)











