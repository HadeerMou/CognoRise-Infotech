import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox

timerwindow = tk.Tk()
timerwindow.geometry('600x600')
timerwindow.configure(background= 'pink')
label = tk.Label(timerwindow, text="countdown", font=('Arial', 30))
label.pack(padx=30,pady=30)

#declare timer variables
hour = StringVar()
minute = StringVar()
second = StringVar()

#set the variables to 00 default value
hour.set('00')
minute.set('00')
second.set('00')

#get user input for time
hourInput = Entry(timerwindow, width=4, font=('Arial', 40, ''), textvariable=hour, justify=CENTER)
minuteInput = Entry(timerwindow, width=4, font=('Arial', 40, ''), textvariable=minute, justify=CENTER)
secondInput = Entry(timerwindow, width=4, font=('Arial', 40, ''), textvariable=second, justify=CENTER)

hourInput.place(x=100, y=200)
minuteInput.place(x=250, y=200)
secondInput.place(x=400, y=200)

#countdown function
def countDown():
    try:
        timer = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print('Invalid values!')

    while(timer > -1):
        totalHour = 0
        totalMinutes, totalSeconds = divmod(timer, 60)
        if(totalMinutes > 60):
            totalHour, totalMinutes = divmod(totalMinutes, 60)

        hour.set('{0:2d}'.format(totalHour))
        minute.set('{0:2d}'.format(totalMinutes))
        second.set('{0:2d}'.format(totalSeconds))

        #update timer
        timerwindow.update()
        time.sleep(1)

        #countdown ending message
        if(timer == 0):
            messagebox.showinfo("", "The Countdown Finished")

        timer -= 1
#starting button
setTimeButton = Button(timerwindow, text='Set Timer',font=30, bd='5', command=countDown)
setTimeButton.place(relx=0.5, rely=0.6, anchor=CENTER)


timerwindow.mainloop()
