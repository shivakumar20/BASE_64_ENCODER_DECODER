##importing modules

from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.configure(bg="#00b8e6")

#title of the window
root.title("Python Project")


#label

Label(root, text ='ENCODE DECODE', font = 'arial 18 bold',bg="#00b8e6",fg="#ffffff").pack()
Label(root, text ='Python Project', font = 'arial 18 bold',bg="#00b8e6",fg="#ffffff").pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

#################### Label and Button ####################

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE',bg="#00b8e6").place(x= 60,y=60)
Entry(root, font = 'comic 11', textvariable = Text, bg = 'ghost white',justify="center").place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY',bg="#00b8e6").place(x=60, y = 90)
Entry(root, font = 'comic 11', textvariable = private_key , bg ='ghost white',justify="center").place(x=290, y = 90)

#mode
mode.set("e")
Radiobutton(root,font = 'arial 10 bold',text="Encode", variable=mode, value='e',bg="#00b8e6",fg="ghostwhite",selectcolor="black").place(x=285, y = 120)
Radiobutton(root,font = 'arial 10 bold',text="Decode", variable=mode, value='d',bg="#00b8e6",fg="ghostwhite",selectcolor="black").place(x=360, y = 120)

#result
Entry(root, font = 'comic 15 italic', textvariable = Result, bg ='ghost white',justify="center").place(x=258, y = 150)

######result button
Button(root, font = 'arial 10 bold', text = 'RESULT',bg="OrangeRed",fg="#ffffff",command = Mode).place(x=62, y = 150)

#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=62, y = 195)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2).place(x=180, y = 195)
root.mainloop()