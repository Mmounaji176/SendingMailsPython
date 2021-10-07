
from tkinter import filedialog
import tkinter as tk
from tkinter import Entry, Message, StringVar, font
from tkinter.constants import COMMAND, END
from PIL import Image,ImageTk
import smtplib
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


user_mail = os.environ.get('email')
user_password = os.environ.get('password')

# set up the info
sender = user_mail
password=user_password

#Create an instance of tkinter frame
win = tk.Tk()

#Set the geometry of tkinter frame
win.geometry("620x600")
win.title("GeteWay Energies")
#Create a canvas
canvas= tk.Canvas(win, width= 600, height= 300)
canvas.grid(columnspan=3 , rowspan=3)


#Load an image in the script
img= (Image.open("logoemail.png"))

#Resize the Image using resize method
logo= img.resize((300,200), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image= logo
logo_label.grid(column=1, row=0)
#entry valiables
sub = StringVar()
msg= StringVar()
path = StringVar()
# entry labels
tk.Label(win,text="Subject :",font=("calibri",13)).grid(columnspan=3,row=1)
SubjectEntry = Entry(win , textvariable=sub , width=30)
SubjectEntry.grid(columnspan=3, column=0, row=2)
tk.Label(win, text="The Message :",font=("calibri",13)).grid(columnspan=3,row=3)
MessageEntry = Entry(win, textvariable=msg , width=50)
MessageEntry.grid(columnspan=3 ,row=4 )
tk.Label(win, text="Browse For Attachement :",font=("calibri",13)).grid(columnspan=3,row=5)
br= StringVar()
br_btn = tk.Button(bg="#281FA6", command=lambda:browse(), fg="white",font=("calibri",15),textvariable=br,height=1,width=7)
br_btn.grid(columnspan=3, row=6 ,pady=10)

br.set("Brows")
#tk.Label(win, text="The attachement's path :", font=("calibri",13)).grid(columnspan=3,row=5)
#PathEntry = Entry(win, textvariable=path , width=50)
#PathEntry.grid(columnspan=3 ,row=6 , pady=10)
file=""
def browse():
    global file
    file = filedialog.askopenfilename()
    tk.Label(win, text=file,font=("calibri",13)).grid(columnspan=3,row=7)
    

send= StringVar()
send_btn = tk.Button(bg="#281FA6", command=lambda:send_mails(), fg="white",font=("calibri",15),textvariable=send,height=2,width=17)
send_btn.grid(columnspan=3, row=8 ,pady=15)
send.set("send")
#clear button
res = StringVar()
reset=tk.Button(bg="#281FA6" ,command=lambda:clear(),fg="white",textvariable=res,height=2,width=8)
reset.grid(columnspan=3, row=9 )
res.set("Clear All")




def clear():
   
    MessageEntry.delete(0,END)
    SubjectEntry.delete(0,END)
def send_mails():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(user_mail,user_password)
    email_send =["mehdilahrach89@gmail.com","mounajimouad@gmail.com"]
    filename=file
    j=9
    for i in email_send:
        j+=1
        msg = MIMEMultipart()
        msg['From'] = user_mail
        msg['To'] = i
        msg['Subject'] = SubjectEntry.get()


        body = MessageEntry.get()
        msg.attach(MIMEText(body,'plain'))

        attachment =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server.sendmail(user_mail,i,text)
        tk.Label(text=("email has been sent to : ",i)).grid(columnspan=3,row=j)


    server.quit()

win.mainloop()
