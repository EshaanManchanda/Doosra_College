import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('eshaanmanchanda01@gmail.com','eshaan123@@')
server.sendmail('eshaanmanchanda01@gmail.com','techlovev@gmail.com',' Hi I am eshaan manchnada i am testing mail bot')