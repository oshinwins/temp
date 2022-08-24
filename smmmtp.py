import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('honeyramteke5@gmail.com', 'Honey@12#76')
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, your otp is '+str(otp)
server.sendmail('honeyramteke5@gmail.com', 'makynlee03@mixtureqg.com', msg)
server.quit()
