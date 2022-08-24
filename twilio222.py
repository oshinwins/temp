from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox


class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x550+10+10')
        self.Labels()
        self.Entry()
    def submit(self):
        print("submitted")

    def resend(self):
        print("resend otp")
        self.resizable(False,False)
        self.n=random.randint(1000,9999)
        self.client=Client("AC61a619ab420082394c78f3868f1bc68e","98b7407a353831482934d6c97c6db767")
        self.client.messages.create(to =["+917758955039"],
                                    from_="+12544002882",
                                    body=f"Your OTP is {self.n}")

    def Labels(self):
        self.c=Frame(self, bg="white", width=400, height=280)
        # self.c.place(x=100,y=60)

        self.Login_Title=Label(self,text="OTP Verification",font="bold,20",bg="white").pack()
        # self.Login_Title.place(x=210,y=90)

        self.c.pack()


    def Entry(self):
        self.User_Name=Text(self,borderwidth=2,wrap="word",width=29,height=2)
        self.User_Name.place(x=190,y=160)

        b1=Button(text="Submit",fg="red",bg="white",font="time 15 bold",width=34,command=self.checkOTP)
        b1.pack(side=LEFT,padx=23)

        b2= Button(text="Resend", fg="red", bg="white", font="time 15 bold", width=34,command=self.resendOTP)
        b2.pack(side=BOTTOM,padx=23)


    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0,"end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo","login success")
                self.n="done"
            elif self.n=="done":
                messagebox.showinfo("showinfo","already login")
            else:
                messagebox.showinfo("showinfo", "wrong otp")
        except:
                messagebox.showinfo("showinfo", "invalid otp")

    def resendOTP(self):
        self.n=random.randint(1000,9999)
        self.client=Client("AC61a619ab420082394c78f3868f1bc68e","98b7407a353831482934d6c97c6db767")
        self.client.messages.create(to =["+917758955039"], from_="+12544002882", body=self.n)


if __name__ == "__main__":
    window = otp_verifier()
    window.mainloop()


