import socket
import sys
import csv
import time
from positiontrans import *
import tkinter as tk
from tkinter import *

HOST = "192.168.0.242" # The remote host
PORT = 30002  # The same port as used by the server
PORT_502 = 502
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


root = tk.Tk()
root.title("Testing")
def myClick():
    root.quit()

def yesClick(yes):
    global a
    a = yes
    root.quit()
def noClick(no):
    global a
    a = no
    root.quit()
def frameClick(frame):
    global b
    b = frame
    root.quit()
def coordinateClick(coordinate):
    global c
    c = coordinate
    root.quit()
def valueClick(data):
    global d
    d = data
    root.quit()

def setXX(data):
    global xx
    xx = data
    root.quit()
def setYY(data):
    global yy
    yy = data
    root.quit()
def setStepx(data):
    global stepx
    stepx = data
    root.quit()

def setStepy(data):
    global stepy
    stepy = data
    root.quit()


myLabel2 = Label(root,text = "bring the robot to the start position(right down corner)", borderwidth=5)
myLabel2.grid(row=0,column=0)
myButton1 = Button(root, text ="Start", command=myClick,padx=25, pady=20)
myButton1.grid(row=2,column=0)

root.mainloop()



start = 0
point = 0
while (point == 0):

    if (start == 0):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT_502))
        print ("")
        reg_400 = ""
        s.send (b"\x00\x04\x00\x00\x00\x06\x00\x03\x01\x90\x00\x01") #request data from register 128-133 (cartisian data)
        reg_400 = s.recv(1024)
        reg_400 = reg_400.replace (b"\x00\x04\x00\x00\x00\x05\x00\x03\x02", b"")
        reg_400 = reg_400.hex() #convert the data from \x hex notation to plain hex
        if reg_400 == "":
          reg_400 = "0000"
        reg_400_i = int(reg_400,16)
        if reg_400_i < 32768:
          reg_400_f = float(reg_400_i)/10
        if reg_400_i > 32767:
          reg_400_i = 65535 - reg_400_i
          reg_400_f = float(reg_400_i)/10*-1
        print ("X  = ",reg_400_f)

        reg_401 = ""
        s.send (b"\x00\x04\x00\x00\x00\x06\x00\x03\x01\x91\x00\x01") #request data from register 128-133 (cartisian data)
        reg_401 = s.recv(1024)
        reg_401 = reg_401.replace (b"\x00\x04\x00\x00\x00\x05\x00\x03\x02", b"")
        reg_401 = reg_401.hex()#convert the data from \x hex notation to plain hex
        if reg_401 == "":
          reg_401 = "0000"
        reg_401_i = int(reg_401,16)
        if reg_401_i < 32768:
          reg_401_f = float(reg_401_i)/10
        if reg_401_i > 32767:
          reg_401_i = 65535 - reg_401_i
          reg_401_f = float(reg_401_i)/10*-1
        print ("Y  = ",reg_401_f)

        reg_402 = ""
        s.send (b"\x00\x04\x00\x00\x00\x06\x00\x03\x01\x92\x00\x01") #request data from register 128-133 (cartisian data)
        reg_402 = s.recv(1024)
        reg_402 = reg_402.replace (b"\x00\x04\x00\x00\x00\x05\x00\x03\x02", b"")
        reg_402 = reg_402.hex() #convert the data from \x hex notation to plain hex
        if reg_402 == "":
          reg_402 = "0000"
        reg_402_i = int(reg_402,16)
        if reg_402_i < 32768:
           reg_402_f = float(reg_402_i)/10
        if reg_402_i > 32767:
           reg_402_i = 65535 - reg_402_i
           reg_402_f = float(reg_402_i)/10*-1
        print ("Z  = ",reg_402_f)

        reg_403 = ""
        reg_403_i = 0
        s.send (b"\x00\x04\x00\x00\x00\x06\x00\x03\x01\x93\x00\x01") #request data from register 128-133 (cartisian data)
        reg_403 = s.recv(1024)
        reg_403 = reg_403.replace (b"\x00\x04\x00\x00\x00\x05\x00\x03\x02", b"")
        reg_403 = reg_403.hex() #convert the data from \x hex notation to plain hex
        if reg_403 == "":
          reg_403 = "0000"
        reg_403_i = int(reg_403,16)
        if reg_403_i < 32768:
           reg_403_f = float(reg_403_i)/1000
        if reg_403_i > 32767:
           reg_403_i = 65535 - reg_403_i
           reg_403_f = float(reg_403_i)/1000*-1
        print ("Rx = ",reg_403_f)

        reg_404 = ""
        reg_404_i = 0
        s.send (b"\x00\x04\x00\x00\x00\x06\x00\x03\x01\x94\x00\x01") #request data from register 128-133 (cartisian data)
        reg_404 = s.recv(1024)
        reg_404 = reg_404.replace (b"\x00\x04\x00\x00\x00\x05\x00\x03\x02", b"")
        reg_404 = reg_404.hex() #convert the data from \x hex notation to plain hex
        if reg_404 == "":
           reg_404 = "0000"
        reg_404_i = int(reg_404,16)
        if reg_404_i < 32768:
           reg_404_f = float(reg_404_i)/1000
        if reg_404_i > 32767:
           reg_404_i = 65535 - reg_404_i
           reg_404_f = float(reg_404_i)/1000*-1
        print ("Ry = ",reg_404_f)

        reg_405 = ""
        reg_405_i = 0
        s.send (b"\x00\x04\x00\x00\x00\x06\x00\x03\x01\x95\x00\x01") #request data from register 128-133 (cartisian data)
        reg_405 = s.recv(1024)
        reg_405 = reg_405.replace (b"\x00\x04\x00\x00\x00\x05\x00\x03\x02", b"")
        reg_405 = reg_405.hex()#convert the data from \x hex notation to plain hex
        if reg_405 == "":
           reg_405 = "0000"
        reg_405_i = int(reg_405,16)
        if reg_405_i < 32768:
           reg_405_f = float(reg_405_i)/1000
        if reg_405_i > 32767:
           reg_405_i = 65535 - reg_405_i
           reg_405_f = float(reg_405_i)/1000*-1
        print ("Rz = ",reg_405_f)

        start = start + 1
        s.close()
        print("port 502 closed")


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    myLabel3 = Label(root, text="current position of the robot:[%s, %s, %s, %s, %s, %s]"%(reg_400_f,reg_401_f,reg_402_f,reg_403_f,reg_404_f,reg_405_f), borderwidth=5)
    myLabel3.grid(row=3, column=0)
    myLabel4 = Label(root, text='1. Is the robot placed in correct position?', borderwidth=5)
    myLabel4.grid(row=4, column=0)
    myButton2 = Button(root, text="Yes", command=lambda *args: yesClick("yes"), padx=25, pady=20)
    myButton2.grid(row=4, column=1)
    myButton3 = Button(root, text="No", command=lambda *args: noClick("no"), padx=25, pady=20)
    myButton3.grid(row=4, column=2)
    root.mainloop()

    m = 0
    if a == 'yes':
        left_down_corner = [reg_400_f/1000,reg_401_f/1000,reg_402_f/1000,reg_403_f,reg_404_f,reg_405_f]
        print("left_down_corner:", left_down_corner)
        point = 1
        print("Position saved", "\n")
        print("number of saved points: ", point, "\n")

    while a == 'no':

        if m==0:
            x = float(reg_400_f)
            y = float(reg_401_f)
            z = float(reg_402_f)
            rx = float(reg_403_f)
            ry = float(reg_404_f)
            rz = float(reg_405_f)
            p = [x/1000,y/1000,z/1000,rx,ry,rz]
        else:
            p = current
        myLabel5 = Label(root, text='2. Would you like to change according to base or tool?', borderwidth=5)
        myLabel5.grid(row=5, column=0)
        myButton4 = Button(root, text="base", command=lambda *args: frameClick("base"), padx=25, pady=20)
        myButton4.grid(row=5, column=1)
        myButton5 = Button(root, text="tool", command=lambda *args: frameClick("tool"), padx=25, pady=20)
        myButton5.grid(row=5, column=2)
        root.mainloop()

        if b == 'tool':
            myLabel6 = Label(root, text='3. Which coordinate would you like to change??', borderwidth=5)
            myLabel6.grid(row=6, column=0)
            myButton6 = Button(root, text="X", command=lambda *args: coordinateClick("x"), padx=25, pady=20)
            myButton6.grid(row=6, column=1)
            myButton7 = Button(root, text="Y", command=lambda *args: coordinateClick("y"), padx=25, pady=20)
            myButton7.grid(row=6, column=2)
            myButton8 = Button(root, text="Z", command=lambda *args: coordinateClick("z"), padx=25, pady=20)
            myButton8.grid(row=6, column=3)
            myButton9 = Button(root, text="RX", command=lambda *args: coordinateClick("rx"), padx=25, pady=20)
            myButton9.grid(row=6, column=4)
            myButton10 = Button(root, text="RY", command=lambda *args: coordinateClick("ry"), padx=25, pady=20)
            myButton10.grid(row=6, column=5)
            myButton11 = Button(root, text="RZ", command=lambda *args: coordinateClick("rz"), padx=25, pady=20)
            myButton11.grid(row=6, column=6)
            root.mainloop()

            myLabel7 = Label(root, text='4. choose the amount of change:', borderwidth=5)
            myLabel7.grid(row=7, column=0)
            myButton12 = Button(root, text="+10", command=lambda *args: valueClick(10), padx=25, pady=20)
            myButton12.grid(row=7, column=1)
            myButton13 = Button(root, text="+5", command=lambda *args: valueClick(5), padx=25, pady=20)
            myButton13.grid(row=7, column=2)
            myButton14 = Button(root, text="+1", command=lambda *args: valueClick(1), padx=25, pady=20)
            myButton14.grid(row=7, column=3)
            myButton15 = Button(root, text="-1", command=lambda *args: valueClick(-1), padx=25, pady=20)
            myButton15.grid(row=7, column=4)
            myButton16 = Button(root, text="-5", command=lambda *args: valueClick(-5), padx=25, pady=20)
            myButton16.grid(row=7, column=5)
            myButton17 = Button(root, text="-10", command=lambda *args: valueClick(-10), padx=25, pady=20)
            myButton17.grid(row=7, column=6)
            root.mainloop()

            if c == 'x':
                d = float(d)
                pose1 = Pose(p)
                x_step = [d/ 1000, 0.0, 0.0, 0.0, 0.0, 0.0]
                pose2 = Pose(x_step)
                finalny = pose1.pose_trans(pose2)
                current = finalny.converter()
                print("after change x", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
            elif c=='y':
                d = float(d)
                pose1 = Pose(p)
                y_step = [ 0.0, d/1000, 0.0, 0.0, 0.0, 0.0]
                pose2 = Pose(y_step)
                finalny = pose1.pose_trans(pose2)
                current = finalny.converter()
                print("after change y", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
            elif c == 'z':
                d = float(d)
                pose1 = Pose(p)
                z_step = [0.0, 0.0, d/1000, 0.0, 0.0, 0.0]
                pose2 = Pose(z_step)
                finalny = pose1.pose_trans(pose2)
                current = finalny.converter()
                print("after change z", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
            elif c == 'rx':
                d = float(d)
                rxx = deg2rad(d)
                pose1 = Pose(p)
                rxx_angle = [0.0 , 0.0, 0.0, rxx, 0.0, 0.0]
                pose2 = Pose(rxx_angle)
                finalny = pose1.pose_trans(pose2)
                current = finalny.converter()
                print("after change rx", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
            elif c == 'ry':
                d = float(d)
                ryy = deg2rad(d)
                pose1 = Pose(p)
                ryy_angle = [0.0, 0.0, 0.0, 0.0, ryy, 0.0]
                pose2 = Pose(ryy_angle)
                finalny = pose1.pose_trans(pose2)
                current = finalny.converter()
                print("after change ry", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                          current[4], current[5]).encode() + b"\n")
            elif c == 'rz':
                d = float(d)
                rzz = deg2rad(d)
                pose1 = Pose(p)
                rzz_angle = [0.0, 0.0, 0.0, 0.0, 0.0, rzz]
                pose2 = Pose(rzz_angle)
                finalny = pose1.pose_trans(pose2)
                current = finalny.converter()
                print("after change rz", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")

        elif b== 'base':
            myLabel6 = Label(root, text='3. Which coordinate would you like to change??', borderwidth=5)
            myLabel6.grid(row=6, column=0)
            myButton6 = Button(root, text="X", command=lambda *args: coordinateClick("x"), padx=25, pady=20)
            myButton6.grid(row=6, column=1)
            myButton7 = Button(root, text="Y", command=lambda *args: coordinateClick("y"), padx=25, pady=20)
            myButton7.grid(row=6, column=2)
            myButton8 = Button(root, text="Z", command=lambda *args: coordinateClick("z"), padx=25, pady=20)
            myButton8.grid(row=6, column=3)
            myButton9 = Button(root, text="RX", command=lambda *args: coordinateClick("rx"), padx=25, pady=20)
            myButton9.grid(row=6, column=4)
            myButton10 = Button(root, text="RY", command=lambda *args: coordinateClick("ry"), padx=25, pady=20)
            myButton10.grid(row=6, column=5)
            myButton11 = Button(root, text="RZ", command=lambda *args: coordinateClick("rz"), padx=25, pady=20)
            myButton11.grid(row=6, column=6)
            root.mainloop()

            myLabel7 = Label(root, text='4. choose the value about which you would like to change:', borderwidth=5)
            myLabel7.grid(row=7, column=0)
            myButton12 = Button(root, text="+10", command=lambda *args: valueClick(10), padx=25, pady=20)
            myButton12.grid(row=8, column=0)
            myButton13 = Button(root, text="+5", command=lambda *args: valueClick(5), padx=25, pady=20)
            myButton13.grid(row=8, column=1)
            myButton14 = Button(root, text="+1", command=lambda *args: valueClick(1), padx=25, pady=20)
            myButton14.grid(row=8, column=2)
            myButton15 = Button(root, text="-1", command=lambda *args: valueClick(-1), padx=25, pady=20)
            myButton15.grid(row=8, column=3)
            myButton16 = Button(root, text="-5", command=lambda *args: valueClick(-5), padx=25, pady=20)
            myButton16.grid(row=8, column=4)
            myButton17 = Button(root, text="-10", command=lambda *args: valueClick(-10), padx=25, pady=20)
            myButton17.grid(row=8, column=5)
            root.mainloop()

            if c == 'x':
                d = float(d)
                x_step = [d / 1000, 0.0, 0.0, 0.0, 0.0, 0.0]
                p[0] = p[0] + x_step[0]
                current = p
                print("after change x", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
            elif c == 'y':
                d = float(d)
                y_step = [0.0, d / 1000, 0.0, 0.0, 0.0, 0.0]
                p[1] = p[1] + y_step[1]
                current = p
                print("after change y", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                         current[4], current[5]).encode() + b"\n")
            elif c == 'z':
                d = float(d)
                z_step = [0.0, 0.0, d / 1000, 0.0, 0.0, 0.0]
                p[2] = p[2] + z_step[2]
                current = p
                print("after change z", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                          current[4], current[5]).encode() + b"\n")
            elif c == 'rx':
                d = float(d)
                rxx = deg2rad(d)
                rxx_angle = [0.0, 0.0, 0.0, rxx, 0.0, 0.0]
                p[3] = p[3] + rxx_angle[3]
                current = p
                print("after change rx", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                          current[4], current[5]).encode() + b"\n")
            elif c == 'ry':
                d = float(d)
                ryy = deg2rad(d)
                ryy_angle = [0.0, 0.0, 0.0, 0.0, ryy, 0.0]
                p[4] = p[4] + ryy_angle[4]
                current = p
                print("after change ry", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
            elif c == 'rz':
                d = float(d)
                rzz = deg2rad(d)
                rzz_angle = [0.0, 0.0, 0.0, 0.0, 0.0, rzz]
                p[5] = p[5] + rzz_angle[5]
                current = p
                print("after change rz", current)
                s.send("movel(p[{},{},{},{},{},{}], a=0.5, v=0.05)".format(current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]).encode() + b"\n")
        m = m +1
        myLabel20 = Label(root, text="current position of the robot:[%s, %s, %s, %s, %s, %s]" % (current[0], current[1], current[2], current[3],
                                                                           current[4], current[5]), borderwidth=5)
        myLabel20.grid(row=9, column=0)
        myLabel21 = Label(root, text='If the robot is placed in correct position click yes, if not repeat step 1-4', borderwidth=5)
        myLabel21.grid(row=10, column=0)
        myButton20 = Button(root, text="Yes", command=lambda *args: yesClick("yes"), padx=25, pady=20)
        myButton2.grid(row=10, column=1)
        myLabel4 = Label(root, text='1. Is the robot placed in correct position?', borderwidth=5)
        myLabel4.grid(row=4, column=0)
        myButton2 = Button(root, text="Yes", command=lambda *args: yesClick("yes"), padx=25, pady=20)
        myButton2.grid(row=4, column=1)
        myButton3 = Button(root, text="No", command=lambda *args: yesClick("no"), padx=25, pady=20)
        myButton3.grid(row=4, column=2)
        root.mainloop()

        if a == 'yes':
            left_down_corner = current
            print("left_down_corner:",left_down_corner)
            point = 1
            print("Position saved" ,"\n")
            print("number of saved points: ", point,"\n")

point1 = left_down_corner

with open('results.csv', 'w') as csvfile:
 spamwriter = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
 spamwriter.writerow(['time','X','Y','Z','RX','RY','RZ'])

a = 1
if a == 1:
    myLabel22 = Label(root, text='How many horizontal points in a row?',borderwidth=5)
    myLabel22.grid(row=11, column=0)
    myButton21 = Button(root, text="5", command=lambda *args: setXX(5), padx=25, pady=20)
    myButton21.grid(row=11, column=1)
    myButton22 = Button(root, text="10", command=lambda *args: setXX(10), padx=25, pady=20)
    myButton22.grid(row=11, column=2)
    myButton23 = Button(root, text="15", command=lambda *args: setXX(15), padx=25, pady=20)
    myButton23.grid(row=11, column=3)
    myButton233 = Button(root, text="20", command=lambda *args: setXX(20), padx=25, pady=20)
    myButton233.grid(row=11, column=4)
    myButton234 = Button(root, text="50", command=lambda *args: setXX(50), padx=25, pady=20)
    myButton234.grid(row=11, column=5)
    myButton235 = Button(root, text="100", command=lambda *args: setXX(100), padx=25, pady=20)
    myButton235.grid(row=11, column=6)

    root.mainloop()

    myLabel23 = Label(root, text='how many vertical layers?',borderwidth=5)
    myLabel23.grid(row=12, column=0)
    myButton24 = Button(root, text="5", command=lambda *args: setYY(5), padx=25, pady=20)
    myButton24.grid(row=12, column=1)
    myButton25 = Button(root, text="10", command=lambda *args: setYY(10), padx=25, pady=20)
    myButton25.grid(row=12, column=2)
    myButton26 = Button(root, text="15", command=lambda *args: setYY(15), padx=25, pady=20)
    myButton26.grid(row=12, column=3)
    myButton268 = Button(root, text="20", command=lambda *args: setYY(20), padx=25, pady=20)
    myButton268.grid(row=12, column=4)
    myButton267 = Button(root, text="50", command=lambda *args: setYY(50), padx=25, pady=20)
    myButton267.grid(row=12, column=5)
    myButton266 = Button(root, text="100", command=lambda *args: setYY(100), padx=25, pady=20)
    myButton266.grid(row=12, column=6)

    root.mainloop()
    myLabel24 = Label(root, text='What should be step in X axis in mm?',borderwidth=5)
    myLabel24.grid(row=11, column=7)
    myButton27 = Button(root, text="1", command=lambda *args: setStepx(1), padx=25, pady=20)
    myButton27.grid(row=11, column=8)
    myButton28 = Button(root, text="2", command=lambda *args: setStepx(2), padx=25, pady=20)
    myButton28.grid(row=11, column=9)
    myButton29 = Button(root, text="5", command=lambda *args: setStepx(5), padx=25, pady=20)
    myButton29.grid(row=11, column=10)
    root.mainloop()

    myLabel25 = Label(root, text='What should be step in Y axis in mm?',borderwidth=5)
    myLabel25.grid(row=12, column=7)
    myButton30 = Button(root, text="1", command=lambda *args: setStepy(1), padx=25, pady=20)
    myButton30.grid(row=12, column=8)
    myButton31 = Button(root, text="2", command=lambda *args: setStepy(2), padx=25, pady=20)
    myButton31.grid(row=12, column=9)
    myButton32 = Button(root, text="5", command=lambda *args: setStepy(5), padx=25, pady=20)
    myButton32.grid(row=12, column=10)
    root.mainloop()

    x = int(xx)
    y = int(yy)
    step_x = int(stepx)
    step_y = int(stepy)

    point1 = left_down_corner
    x_step = [step_x/1000, 0.0, 0.0, 0.0,0.0,0.0]
    x_step3 = [-step_x/ 1000, 0.0, 0.0, 0.0, 0.0, 0.0]
    y_step = [0.0, -step_y/ 1000, 0.0, 0.0, 0.0, 0.0]
    pose1 = Pose(point1)
    current = left_down_corner
    time.sleep(0.1)
    s.send(b"set_analog_out(1, 0.33)" + b"\n")
    start_time = time.time()
    point_time = 0.0

    with open('results.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([point_time, current[0], current[1], current[2], current[3], current[4], current[5]])

    a = a + 1
    print("record finish")
    time.sleep(0.1)
    s.send(b"set_analog_out(1, 0.0)" + b"\n")
    time.sleep(0.05)
    n = 1
    print("n=", n)
    m = 1
    counter = 1

    pose1 = Pose(current)
    pose2 = Pose(x_step)
    pose3 = Pose(x_step3)
    pose4 = Pose(y_step)

    while m <= y:
        while n<x:
            if m%2 == 0:
                finalny = pose1.pose_trans(pose2)
                print("current point",finalny)
            else:
                finalny = pose1.pose_trans(pose3)
                print("current point", finalny)
            current = finalny.converter()
            s.send("movel(p[{},{},{},{},{},{}], a=0.2, v=0.02)".format(current[0],current[1],current[2],current[3],current[4],current[5]).encode() + b"\n")

            time.sleep(0.2)
            s.send(b"set_analog_out(1, 0.33)" + b"\n")
            current_time = time.time()
            point_time  = round(current_time - start_time,3)
            with open('results.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([point_time,current[0], current[1], current[2], current[3],current[4], current[5]])

            a = a + 1
            print("record finish")
            n=n+1
            print("n=",n)
            time.sleep(0.05)
            s.send(b"set_analog_out(1, 0.0)" + b"\n")
            time.sleep(0.05)
            pose1 = Pose(current)
            counter = counter +1
            if n== x and m == y:
                print("number of scanned points in grid:", counter)
                sys.exit()
        while n>=x :
            finalny= pose1.pose_trans(pose4)
            current = finalny.converter()
            s.send("movel(p[{},{},{},{},{},{}], a=0.2, v=0.02)".format(current[0], current[1], current[2], current[3],current[4], current[5]).encode() + b"\n")
            time.sleep(0.1)
            s.send(b"set_analog_out(1, 0.33)" + b"\n")
            current_time = time.time()
            point_time = round(current_time - start_time, 3)

            with open('results.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    [point_time, current[0], current[1], current[2], current[3], current[4], current[5]])

            a = a + 1
            print("record finish")
            time.sleep(0.05)

            s.send(b"set_analog_out(1, 0.0)" + b"\n")
            time.sleep(0.05)

            pose1 = Pose(current)
            m = m + 1
            print("m=",m)
            n = 1
            print("n=", n)
            counter = counter + 1