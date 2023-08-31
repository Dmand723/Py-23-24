#Dawson Simmons
#Alarm Clock Main Script  
#Last Edit 8/25/23

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

def createMilCxBox():
    global milCxBox
    milCxBox = Checkbutton(root, text= "12 Hour Format", command= toggleMil)
    milCxBox.place(x = 20, y= 20)
    milCxBox
    #btn1 = Button(root, text= H24_H12 , bd= 5, command=switchAMPM())
    #btn1.pack(side= 'top')

def createPlyBtn():
    playBtn = Button(root, text= "Test sound", command=playAlarm)
    playBtn.place(x=3,y=3)

def playAlarm():
    alarm1()

def toggleMil():
    global is_mil_time
    is_mil_time = not is_mil_time

def createWidiges():
    global time_lbl
    size = int(HIGHT *.25)
    fnt = font.Font(family="Century Gothic", size=size, weight="bold")
    time_lbl = ttk.Label(root,  textvariable=time_text, foreground= "blue",background= "Black", font= fnt)
    time_lbl.place(x=WIDTH/2, y= HIGHT /2, anchor=CENTER)
    createMilCxBox()
    createPlyBtn()

def runClock():
    time_text.set(getTime(MST))
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
    milCxBox.place(x=10, y = y -30)
    

    

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