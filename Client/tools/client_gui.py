from tkinter import *

class ChatWindow(object):

    def __init__(self):
        self.top = Tk()
        self.top.title('Private talking room')
        self.label = Label(self.top, text='Private talking room')
        self.label.pack()
        self.message_show = Frame(self.top)
        self.message_sr = Scrollbar(self.message_show)
        self.message_sr.pack(side=RIGHT, fill=Y)
        self.message_text = Text(self.message_show, height=20, width=40, font=('Arial', 15))
        self.message_text.config(state=DISABLED)
        self.message_sr.config(command=self.message_text.yview)
        self.message_text.pack(side=LEFT, fill=X)
        self.message_show.pack(anchor=N)

        self.message_input = Frame(self.top)
        self.message_ipt_text = Text(self.message_input, height=25, width=52, font=('Arial', 18))
        self.send_msg = Button(self.message_input, text='Send', command=self.send_message, fg='white', bg='blue')
        self.send_msg.pack(side=RIGHT)
        self.message_ipt_text.pack(side=LEFT, fill=X)
        self.message_input.pack(anchor=N)