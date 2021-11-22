import sys

sys.path.append('..')

from Client.tools import process
from tkinter import *


class LoginWindow(object):
    def __init__(self, Client, ADDR):
        self.top = Tk()
        self.top.title('Private talking room')
        self.top.geometry("800x400")

        self.label = Label(self.top, text='Private talking room', height=10, font=("Arial", 15))
        self.label.pack()

        self.input1 = Frame(self.top)
        self.label1 = Label(self.input1, text='Username', font=("Arial", 15))
        self.input_username = Text(self.input1, height=1, width=15, font=('Arial', 13))
        self.input_username.config(state=NORMAL)
        self.label1.pack(side=LEFT)
        self.input_username.pack(side=RIGHT)
        self.input1.pack(anchor=N)

        self.input2 = Frame(self.top)
        self.label2 = Label(self.input2, text='Password', font=("Arial", 15))
        self.input_password = Text(self.input2, height=1, width=15, font=('Arial', 13))
        self.input_password.config(state=NORMAL)
        self.label2.pack(side=LEFT)
        self.input_password.pack(side=RIGHT)
        self.input2.pack(anchor=N)

        self.buttons = Frame(self.top)
        self.register_button = Button(self.buttons, text='Register', command=self.register, fg='white', bg='blue')
        self.submit_button = Button(self.buttons, text='Login', command=self.submit, fg='white', bg='blue')
        self.register_button.pack(side=LEFT)
        self.submit_button.pack(side=RIGHT)
        self.buttons.pack(anchor=S)
        self.name = ''
        self.state = False
        self.client = Client
        self.addr = ADDR

    def register(self):
        username = self.input_username.get('0.0', END).strip()
        password = self.input_password.get('0.0', END).strip()
        self.input_username.delete('0.0', END)
        self.input_password.delete('0.0', END)
        user_pass = username + ' ' + password
        package = process.assemble('register', 'unknown', 'server', len(user_pass), user_pass)
        self.client.sendto(package, self.addr)
        package, ADDR = self.client.recvfrom(1024)
        sign, s_name, r_name, length, state = process.analyze(package)
        state = state.decode('utf-8')
        if state == 'success':
            print('successful register')
        elif state == 'fail':
            print('register failed')
        else:
            print('error with server')

    def submit(self):
        username = self.input_username.get('0.0', END).strip()
        password = self.input_password.get('0.0', END).strip()
        self.input_username.delete('0.0', END)
        self.input_password.delete('0.0', END)
        user_pass = username + ' ' + password
        package = process.assemble('login', 'unknown', 'server', len(user_pass), user_pass)
        self.client.sendto(package, self.addr)
        package, ADDR = self.client.recvfrom(1024)
        sign, s_name, r_name, length, state = process.analyze(package)
        state = state.decode('utf-8')

        if state == 'success':
            self.name = username
            self.state = True
            self.top.quit()
            self.top.destroy()
        elif state == 'fail':
            print("Wrong username or password")
        else:
            print('error with server')

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

