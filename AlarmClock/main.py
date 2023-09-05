#Dawson Simmons
#Alarm Clock Main Script  
#Last Edit 9/5/23

#Imports
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import font 
from tkinter import ttk
import calendar as cal
import time
from time import sleep as wait
import datetime as dtime
import os 

from assets.scripts.settings import *
from assets.scripts.alarms import *

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#globals---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
running = True
cur_time_str = ""
time_lbl = ""
is_mil_time = True
tag = ""
H24_H12 = ""
milCxBox = ""
ui = ""
low = 0
high = 24
curTZ = MST
timeZoneCb = ""


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#funtions------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funtion that finds the current time 
def  getTime(tz):
    global H24_H12
    global tag
    total_time = cal.timegm(time.gmtime())
    cur_sec = total_time % 60
    total_min = total_time // 60
    cur_min = total_min % 60
    total_hour = total_min // 60
    cur_hour = total_hour % 24 
    cur_hour += tz

    
    if  is_mil_time == False:
        H24_H12 = "12 Hour Format"
        if cur_hour > 12:
            str_hour = str(cur_hour - 12)
        if cur_hour > 11:
            tag = "PM"
        else:
            tag = "AM"
            
   
    
    
    
    if is_mil_time:
        H24_H12 = "24 Hour Format"
        tag = ""

    str_hour = str(cur_hour)
    str_min = str(cur_min)
    str_sec = str(cur_sec)


    if cur_min < 10:
        str_min = "0"+str(cur_min)
    if cur_sec < 10:
        str_sec = "0"+str(cur_sec)
    
    if is_mil_time:

        if cur_hour < 10:
            str_hour = "0"+str(cur_hour)

    
    cur_time_str =str.format("{}:{}:{} {}", str_hour,str_min,str_sec, tag)
    
    
    return cur_time_str



def rootSetup():
    global time_text
    root = Tk()
    root.geometry(geoString)
    root.title(TITLE)
    root.iconbitmap('assets/sprites/clock.ico')
    root.configure(background= ROOT_COLOR)
    
    


    


    
   
    

    
    return root

#Create Main UT box
def createUI():
    global ui
    ui = Frame(root, height=50,width=WIDTH,background="purple")
    ui.place(x=0, y=HIGHT-50)
    ui.pack_propagate(False)

#show the time
def createTimeLbl():
    global time_lbl
    size = int(HIGHT *.25)
    fnt = font.Font(family="Century Gothic", size=size, weight="bold")
    time_lbl = ttk.Label(root,  textvariable=time_text, foreground= "blue",background= "Black", font= fnt)
    time_lbl.place(x=WIDTH/2, y= HIGHT /2, anchor=CENTER)

#Check box for military or std time 
def createMilCxBox():
    global milCxBox
    global ui
    milCxBox = Checkbutton(ui, text= "12 Hour Format", command= toggleMil)
    milCxBox.pack(side= RIGHT)
    
    
    
#Create stop alarm button
def createStopBtn():
    global ui
    stopBtn = Button(ui, text= "Stop", command=stopAlarm, width=10)
    stopBtn.pack(side= LEFT)

#Create Snooz alarm button
def createSnoozBtn():
    stopBtn = Button(ui, text= "Snooz", command=snoozAlarm,width=10)
    stopBtn.pack(side= LEFT)

def createSetBtn():
    stopBtn = Button(ui, text= "Set Alarm", command=setAlarm,width=10)
    stopBtn.pack(side= RIGHT)

def createTimeZoneBtn():
    global timeZoneCb
    timeZoneCb = ttk.Combobox(ui,values=["EST","CST","MST","PST"], justify="center",width=5,height=25)
    timeZoneCb.pack(side = RIGHT)
    timeZoneCb.bind("<<ComboboxSelected>>", setCurTZ)
    timeZoneCb.current(2)

def createAlarmBtns():
    alarmTag = StringVar()

    amCkBox = Radiobutton(ui, text="AM",variable=alarmTag,value="AM" )
    pmCkBox = Radiobutton(ui, text="PM",variable=alarmTag,value="PM")
    amCkBox.pack(side = RIGHT)
    pmCkBox.pack(side =RIGHT)

    alarmHour = Spinbox(ui, from_=low,to=high, justify="center", width=5)
    alarmMin = Spinbox(ui, from_=0,to=59, justify="center", width=5)
    alarmMin.pack(side=RIGHT)
    alarmHour.pack(side=RIGHT)

def setCurTZ(trash):
    global curTZ
    global timeZoneCb
    temp = timeZoneCb.get()
    if temp == "EST":
        curTZ = EST
    elif temp == "MST":
        curTZ = MST
    elif temp == "PST":
        curTZ = PST
    elif temp == "CST":
        curTZ = CST

def playAlarm():
    alarm1()

def stopAlarm():
    print("stop")

def snoozAlarm():
    print("snooz")

def setAlarm():
    print("set")

def toggleMil():
    global is_mil_time
    is_mil_time = not is_mil_time

def createWidiges():
    createUI()

    createTimeLbl()
    createMilCxBox()
    createTimeZoneBtn() 
    createStopBtn()
    createSetBtn()
    createSnoozBtn()
    createAlarmBtns()

    
    

def runClock():
    time_text.set(getTime(curTZ))
    updateWidiges()
    
    



    root.after(1,runClock)

def updateWidiges():
    #get cur window size 
    x = root.winfo_width()
    y = root.winfo_height()

    # size = int(y * .25)
    # fnt = font.Font(family = "Century Gothic" ,size=size , weight= 'bold')
    # time_lbl.config(font=fnt)
    time_lbl.place(x = x/2 , y = y/2, anchor = CENTER)
    ui.config(width=x)
    ui.place(x=0,y=y-50)
    

    

#Main runtime funtion 
def main():
    global time_text
    global root
    root = rootSetup()
    time_text = StringVar()
    time_text.set(getTime(MST))
    createWidiges()
    root.after(1,runClock)


    root.mainloop()


    
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

main()


    




    










































































































































# #prints changeBday
# def changeBDay(yearsToAdd = 0, daysToAdd = 0, mounthsToAdd = 0):
#     global b_day
#     global b_day_year
#     global b_day_month
#     global bday_day
#     b_day_year += yearsToAdd
#     b_day_month += mounthsToAdd
#     bday_day += daysToAdd
#     print(b_day)




# #main funtion
# def main():
#     print("\nHi dad it's "+ name)
#     wait(1)
#     var1 = input("\nWhere did you go? ")
#     print("...")
#     wait(1)
#     print("You suck")
#     wait(1)
#     print("Do you even remeber my birthday?")
#     wait(1)
#     changeBDay(50)
# b_day_month = 7
# bday_day = 23 
# b_day_year = 2006
# b_day = str(b_day_month) + "/" + str(23) + "/" + str(b_day_year)
# name = "Dawson"