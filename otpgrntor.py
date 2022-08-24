import random
generatorotp=random.randint(000000,100000)
username=input("Username:")
print("Hello....!!!",username)
print('here is your otp for login',generatorotp)
password=input("enter the otp for login:")
if password==str(generatorotp):
    print("login success")
else:
    password!=str(generatorotp)
    print("login failed")
