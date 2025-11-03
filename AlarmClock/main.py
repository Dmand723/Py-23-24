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
debug = True


cur_hour = 0
cur_min = 0
cur_sec = 0

running = True
isAlarmsOpen = False
cur_time_str = ""
time_lbl = ""
is_mil_time = True
tag = ""
H24_H12 = ""
milCxBox = ""
ui = ""
alarmsTab = ""
low = 0
high = 24
curTZ = MST
timeZoneCb = ""
amCkBox = ""
pmCkBox = ""
alarmMinSb = ""
alarmHourSb = ""
setBtn = ""
alarmHour = 0
alarmMin = 0

isAlarmMilTime = True
isAlarmOn = False
isAlarmPlaying = False

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#funtions------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funtion that finds the current time 
def  getTime(tz):
    global tag
    global cur_hour
    global cur_min
    global cur_sec
    total_time = cal.timegm(time.gmtime())
    cur_sec = total_time % 60
    total_min = total_time // 60
    cur_min = total_min % 60
    total_hour = total_min // 60
    cur_hour = total_hour % 24 
    cur_hour += tz

    
    if  is_mil_time == False:
        if cur_hour > 12:
            str_hour = str(cur_hour - 12)
        if cur_hour > 11:
            tag = "PM"
        else:
            tag = "AM"
            
   
    
    
    
    if is_mil_time:
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
    #root.iconbitmap('assets/sprites/clock.ico')
    root.configure(background= ROOT_COLOR)
   

    


    
   
    

    
    return root



#Create Main UI box
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
    milCxBox.pack(side= RIGHT,padx=10)

#Create alarms tab
def createAlarmsTab():
    global alarmsTab
    global isAlarmsOpen
    if isAlarmsOpen:
        return
    isAlarmsOpen = True
    alarmsTab = Frame(root, height=70, width=100,background="blue")
    alarmsTab.place(x=0,y=0)
    alarmsTab.pack_propagate(False)
    
    createAlarmBtns()

#Destroy the alarms tab
def hideAlarmsTab():
    global isAlarmsOpen
    isAlarmsOpen = False
    alarmsTab.destroy()



#Create stop alarm button
def createStopBtn():
    stopBtn = Button(ui, text= "Stop", command=stopAlarm, width=10)
    stopBtn.pack(side= LEFT,padx=10)

#Create Snooz alarm button
def createSnoozBtn():
    stopBtn = Button(ui, text= "Snooz", command=snoozAlarm,width=10)
    stopBtn.pack(side= LEFT,padx=10)

def setAlarmBtnFunc():
    createAlarmsTab()

#Create The button to set an alarm 
def createSetBtn(name):
    global setBtn
    setBtn = Button(ui, text= name, command=setAlarmBtnFunc,width=10)
    setBtn.pack(side= RIGHT,padx=10)

#Create the dropdown menu to change the timezone 
def createTimeZoneBtn():
    global timeZoneCb
    timeZoneCb = ttk.Combobox(ui,values=["EST","CST","MST","PST"], justify="center",width=5,height=25)
    timeZoneCb.pack(side = RIGHT,padx=10)
    timeZoneCb.bind("<<ComboboxSelected>>", setCurTZ)
    timeZoneCb.current(2)

#Create the Buttons to change the time of alarm and set alarm 
def createAlarmBtns():
    global amCkBox
    global pmCkBox
    global alarmMinSb
    global alarmHourSb
    alarmTag = StringVar()

    saveAlarmBtn = Button(alarmsTab,text="Save Alarm", command=saveAlarmFunc)
    saveAlarmBtn.pack(side=RIGHT,padx=10)

    amCkBox = Radiobutton(alarmsTab, text="AM",variable=alarmTag,value="AM",justify="center" )
    pmCkBox = Radiobutton(alarmsTab, text="PM",variable=alarmTag,value="PM",justify="center")
    if is_mil_time == False:
        amCkBox.pack(side = RIGHT)
        pmCkBox.pack(side =RIGHT)

    alarmHourSb = Spinbox(alarmsTab, from_=low,to=high, justify="center", width=5)
    alarmMinSb = Spinbox(alarmsTab, from_=0,to=59, justify="center", width=5,)
    alarmMinSb.pack(side=RIGHT,padx=10)
    alarmHourSb.pack(side=RIGHT,padx=10)
    alarmCxBox = Checkbutton(alarmsTab, text= "On", command= toggleAlarm)
    alarmCxBox.pack(side=RIGHT,padx=10)

    



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
    global isAlarmPlaying
    alarm1()
    isAlarmPlaying = True

def stopAlarm():
    isAlarmPlaying = False
    print("stop")

def snoozAlarm():
    print("snooz")

def saveAlarmFunc():
    saveAlarmTime()
    changeSetName()
    hideAlarmsTab()

#Sets the alarmtime
def saveAlarmTime():
    global alarmHour
    global alarmMin
    if is_mil_time:
        isAlarmMilTime = True
    else:
        isAlarmMilTime = False
    alarmHourstr= alarmHourSb.get()
    alarmMinstr = alarmMinSb.get()
    alarmHour = int(alarmHourstr)
    alarmMin = int(alarmMinstr)

def changeSetName(): #Changes the set alarm button name to set new alarm
    setBtn.config(text= "Set New Alarm" ,width=12)

def toggleMil():
    global is_mil_time
    is_mil_time = not is_mil_time
    destroyAmPmCxBox()

def toggleAlarm():
    global isAlarmOn
    isAlarmOn = not isAlarmOn

def destroyAmPmCxBox():
    if is_mil_time & isAlarmsOpen:
        amCkBox.pack_forget()
        pmCkBox.pack_forget()

def createWidiges():
    createUI()
    

    createTimeLbl()
    createMilCxBox()
    createTimeZoneBtn() 
    createStopBtn()
    createSetBtn("Set Alarm")
    createSnoozBtn()
    if debug:
        createDebugBtn()
    
    

    
    

def runClock():
    time_text.set(getTime(curTZ))
    updateWidiges()
    
    



    root.after(1,runClock)
    root.after(10,checkForAlarmTime)

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
    if isAlarmsOpen == True:
        alarmsTab.config(width=x)
        alarmsTab.place(x=0,y=0)
        if is_mil_time == False & isAlarmsOpen:
            amCkBox.pack(before= alarmMinSb, side= RIGHT)
            pmCkBox.pack(before= amCkBox, side= RIGHT)
        
def checkForAlarmTime():
    if (isAlarmOn == True and not isAlarmPlaying):
        if isAlarmMilTime:
            if (alarmHour == cur_hour and alarmMin == cur_min):
                 playAlarm()
        else:
            if (alarmHour == cur_hour -12 and alarmMin == cur_min):
                    playAlarm()
    

    

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

#Creates a button for debuging/testing. Use button for one time calls of something you are testing
def createDebugBtn():
    debugBtn = Button(ui, text="Debug", command=debugPrint)
    debugBtn.pack()

#Function for a debug print statment
def debugPrint():
    print(isAlarmPlaying)
    
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

main()