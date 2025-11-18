import os
import sqlite3
from tkinter import *


# find the current file path
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
dbfile = os.path.join(CURRENT_DIR, "iot_data.db")

# connect with local sqlite3 database or web server database
conn = sqlite3.connect(dbfile, check_same_thread=False)
c = conn.cursor()

# root class
class MainWindow:
    __data = None
    def __init__(self, win):
        self.win = win
        self.create_table()
        self.create_widget()
        self.read_inserted_data()
        
    # bed room light on
    def light_on1(self, event=None):
        self.btn_on1.config(state='disable')
        self.btn_off1.config(state='normal')
        self.update_table('1', 'Room_1')
        
    # bed room light off
    def light_off1(self, event=None):
        self.btn_on1.config(state='normal')
        self.btn_off1.config(state='disable')
        self.update_table('0', 'Room_1')

    # kitchen light on
    def light_on2(self, event=None):
        self.btn_on2.config(state='disable')
        self.btn_off2.config(state='normal')
        self.update_table('1', 'Room_2')
        
    # kitchen light off
    def light_off2(self, event=None):
        self.btn_on2.config(state='normal')
        self.btn_off2.config(state='disable')
        self.update_table('0', 'Room_2')

    # update database for set action or status
    def update_table(self, rm_status, rm_no):
        c.execute("update room_info set [Room Status]='{0}' where [Room No] = '{1}'".format(rm_status, rm_no))
        conn.commit()
        
    # create database table if not exists
    def create_table(self):
        c.execute('create table if not exists room_info([Room No] text, [Room Status] integer)')
        
    # insert default data or read data for action from database
    def read_inserted_data(self):
        default_data = {'Room_1' : 0, 'Room_2' : 0}
        c.execute('select * from room_info')
        data = c.fetchall()
        if data: self.__data = data
        else:
            for k, v in default_data.items():
                c.execute('insert into room_info([Room No], [Room Status]) values(?, ?)', (k, v))
            conn.commit()
            c.execute('select * from room_info')
            self.__data = c.fetchall()
        # show the button status
        for i in range(len(self.__data)):
            if self.__data[i][1]==1:
                eval('self.btn_on'+(str(i+1))).config(state='disable')
                eval('self.btn_off'+(str(i+1))).config(state='normal')
            else:
                eval('self.btn_on'+(str(i+1))).config(state='normal')
                eval('self.btn_off'+(str(i+1))).config(state='disable')
        
        
    # create gui(graphical user interface) widget
    def create_widget(self):
        # create first frame(bed room)
        self.top_frame1 = Frame(self.win)
        self.top_frame1.pack(side=TOP, fill=X)
        self.label1 = Label(self.top_frame1, text='Bed Room', font='Cambria 18 bold italic', bg='blue', fg='white')
        self.label1.pack(side=TOP, pady=(20, 5), fill=X, expand=1)
        self.btn_on1 = Button(self.top_frame1, text='ON', font='Cambria 12 bold', bg='green', fg='white', relief=FLAT, cursor='hand2', width=10, command=lambda:self.light_on1())
        self.btn_on1.pack(side=LEFT, padx=100)
        self.btn_off1 = Button(self.top_frame1, text='OFF', font='Cambria 12 bold', bg='red', fg='white', relief=FLAT, cursor='hand2', width=10, command=lambda:self.light_off1())
        self.btn_off1.pack(side=LEFT, padx=5)

        # create second frame(kitchen)
        self.top_frame2 = Frame(self.win)
        self.top_frame2.pack(side=TOP, fill=X)
        self.label2 = Label(self.top_frame2, text='Kitchen', font='Cambria 18 bold italic', bg='blue', fg='white')
        self.label2.pack(side=TOP, pady=(20, 5), fill=X, expand=1)
        self.btn_on2 = Button(self.top_frame2, text='ON', font='Cambria 12 bold', bg='green', fg='white', relief=FLAT, cursor='hand2', width=10, command=lambda:self.light_on2())
        self.btn_on2.pack(side=LEFT, padx=100)
        self.btn_off2 = Button(self.top_frame2, text='OFF', font='Cambria 12 bold', bg='red', fg='white', relief=FLAT, cursor='hand2', width=10, command=lambda:self.light_off2())
        self.btn_off2.pack(side=LEFT, padx=5)

        
# root
if __name__=='__main__':
    win = Tk()
    win.title('Main Window')
    w = 500; h = 210
    sw = win.winfo_screenwidth() # for center in screen
    sh = win.winfo_screenheight() # for center in screen
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.resizable(0, 0)
    app = MainWindow(win)
    win.mainloop()