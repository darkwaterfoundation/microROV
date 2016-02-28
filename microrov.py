# -*- coding: utf-8 -*-
#!/usr/bin/env python
########################################################################
# This example controls the GoPiGo and using a PS3 Dualshock 3 controller
#
# http://www.dexterindustries.com/GoPiGo/
# History
# ------------------------------------------------
# Author        Date                    Comments
# Karan Nayan   11 July 14              Initial Authoring
'''
## License
 GoPiGo for the Raspberry Pi: an open source robotics platform for the Raspberry Pi.
 Copyright (C) 2015  Dexter Industries

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
import serial, sys, time ,os, math
from ps3 import *               #Import the PS3 library
import scrollphat
from dw640HAT import dw_MotorCONTROL, dw_DCMotor

def showmotor(controller, row, motorval):
        if controller == "ab":
                row = row + 6

        #print motorval

        if motorval == 0:
                for n in range(5):
                        scrollphat.set_pixel(row,n,0)
                        scrollphat.update()
        else:
                steps = int(round((abs(motorval) - BASE_MOTOR_POWER) / 21))
                for n in range(5):
                        if n <= steps:
                                scrollphat.set_pixel(row,n,1)
                                scrollphat.update()
                        else:
                                scrollphat.set_pixel(row,n,0)
                                scrollphat.update()

        return

def toggle(controller):
        #sendcommand(controller.identifier + "-t();")
        return

def timerstart(controller):
        #sendcommand(controller.identifier + "-ts();")
        return

def motor(controller, port, starboard, depth):
        #mleft.setMotorSpeed(port)
        #mright.setMotorSpeed(starboard)
        #mvert.setMotorSpeed(depth)
        #sendcommand(controller.identifier + "-m(" + str(port) + "," + str(starboard) + "," + str(depth) + ");")
        return

def port(controller, speed):
        #print port
        mleft.setMotorSpeed(speed)

        showmotor(controller, 2, speed)

        #print speed
        #sendcommand(controller.identifier + "-p(" + port + ");")
        return

def starboard(controller, speed):
        #print starboard
        mright.setMotorSpeed(speed)

        showmotor(controller, 0, speed)

        #print speed
        #sendcommand(controller.identifier + "-s(" + starboard + ");")
        return

def depth(controller, speed):
        #print depth
        mvert.setMotorSpeed(speed)

        showmotor(controller, 4, speed)

        #print speed
        #sendcommand(controller.identifier + "-v(" + str(depth) + ");")
        return

def direction(controller, port, starboard):
        #mleft.setMotorSpeed(port)
        #mright.setMotorSpeed(starboard)
        #sendcommand(controller.identifier + "-d(" + str(port) + "," + str(starboard) + ");")
        return

def sendcommand( cmd ):
        #print(cmd.encode())
        return

def tolarge( reading ):
        return int(reading * 100)

def calcleftmotor( x, y ):
        #print(x)
        #print(y)
        v = (100 - abs(x)) * (y/100) + y
        #print(v)
        w = (100 - abs(y)) * (x/100) + x
        #print(w)
        speed = (v-w)/2
        #print(speed)
        return int(speed)

def calcrightmotor( x, y ):
        v = (100 - abs(x)) * (y/100) + y
        w = (100 - abs(y)) * (x/100) + x
        speed = (v+w)/2
        #print(speed)
        return int(speed)

def translate(value,leftmin, leftmax, rightmin, rightmax):
        leftspan = leftmax - leftmin
        rightspan = rightmax - rightmin

        scaled = float(value - leftmin) / float(leftspan)
        return int(rightmin + (scaled * rightspan))

# seconds we wait before sending another button press
BUTTON_LAG = 0.5

BASE_MOTOR_POWER = 150

scrollphat.clear()
scrollphat.set_brightness(2)

# The start logo - all bloody for haloween
print(" ███▄ ▄███▓ ██▓ ▄████▄   ██▀███   ▒█████   ██▀███   ▒█████   ██▒   █▓")
print("▓██▒▀█▀ ██▒▓██▒▒██▀ ▀█  ▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒▓██░   █▒")
print("▓██    ▓██░▒██▒▒▓█    ▄ ▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒ ▓██  █▒░")
print("▒██    ▒██ ░██░▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ▒██   ██░  ▒██ █░░")
print("▒██▒   ░██▒░██░▒ ▓███▀ ░░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒░ ████▓▒░   ▒▀█░  ")
print("░ ▒░   ░  ░░▓  ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░    ░ ▐░  ")
print("░  ░      ░ ▒ ░  ░  ▒     ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░    ░ ░░  ")
print("░      ░    ▒ ░░          ░░   ░ ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒       ░░  ")
print("       ░    ░  ░ ░         ░         ░ ░     ░         ░ ░        ░  ")
print("               ░                                                 ░   ")


print("Initializing...")

print("Attaching Motors")
dw = dw_MotorCONTROL( addr=0x60 )
# Swap for different address if also using scrollphat
#dw = dw_MotorCONTROL( addr=0x61 )
mleft = dw.getMotor(2)
mright = dw.getMotor(1)
mvert = dw.getMotor(3)

controllerlist = []

# create a ps3 object - we want to handle up to two controllers
p=ps3()         #Create a PS3 object
if p.joystick_count == 1:
        print("Found controller 1 - ")
        p.select_joystick(0)
        controllerlist.append(p)
        print("Setting ID to " + p.identifier)
elif p.joystick_count == 2:
        print("Found controller 1 - ")
        p.select_joystick(0)
        controllerlist.append(p)
        print("Setting ID to " + p.identifier)
        ptwo=ps3()
        print("Found controller 2 - ")
        ptwo.select_joystick(1)
        controllerlist.append(ptwo)
        print("Setting ID to " + ptwo.identifier)

print("Ready")
s=150   #Initialize
run=1
flag=0
tolerance=0.01
while True:
    try:
        for ps in controllerlist:
                ps.update()                     #Read the ps3 values
                if ps.select:
                        # Select toggle button pressed
                        if (time.time() - ps.lastbuttontime) > BUTTON_LAG or ps.lastbuttontime == 0:
                                ps.lastbuttontime = time.time()
                                toggle(ps)
                elif ps.start:
                        # Start / stop timer button pressed
                        if (time.time() - ps.lastbuttontime) > BUTTON_LAG or ps.lastbuttontime == 0:
                                ps.lastbuttontime = time.time()
                                timerstart(ps)

                if ps.r1:
                        if (time.time() - ps.lastbuttontime) > BUTTON_LAG or ps.lastbuttontime == 0:
                                ps.lastbuttontime = time.time()
                                motordepth = -255
                                if motordepth != ps.lastvert:
                                        ps.lastvert = motordepth
                                        depth(ps, motordepth)
                elif ps.r2:
                        if (time.time() - ps.lastbuttontime) > BUTTON_LAG or ps.lastbuttontime == 0:
                                ps.lastbuttontime = time.time()
                                motordepth = 255
                                if motordepth != ps.lastvert:
                                        ps.lastvert = motordepth
                                        depth(ps, motordepth)
                else:
                        motordepth = 0
                        if motordepth != ps.lastvert:
                                ps.lastvert = motordepth
                                depth(ps, motordepth)


                lefty=(ps.a_joystick_left_y)
                righty=(ps.a_joystick_right_y)

                # control the left motor
                if abs(lefty) > tolerance:
                        motorleft = -translate(tolarge(lefty), -100, 100, -255, 255)
                        if motorleft > 0 and motorleft < BASE_MOTOR_POWER:
                                motorleft = BASE_MOTOR_POWER
                        elif motorleft <0 and abs(motorleft) < BASE_MOTOR_POWER:
                                motorleft = -BASE_MOTOR_POWER

                        if motorleft != ps.lastleft:
                                port(ps, motorleft)
                                ps.lastleft = motorleft
                else:   # at rest
                        motorleft = 0
                        if motorleft != ps.lastleft:
                                port(ps, motorleft)
                                ps.lastleft = motorleft


                # control the right motor
                if abs(righty) > tolerance:
                        motorright = -translate(tolarge(righty), -100, 100, -255, 255)
                        if motorright > 0 and motorright < BASE_MOTOR_POWER:
                                motorright = BASE_MOTOR_POWER
                        elif motorright <0 and abs(motorright) < BASE_MOTOR_POWER:
                                motorright = -BASE_MOTOR_POWER

                        if motorright != ps.lastright:
                                starboard(ps,motorright)
                                ps.lastright = motorright
                else:
                        # at rest
                        motorright = 0
                        if motorright != ps.lastright:
                                starboard(ps,motorright)
                                ps.lastright = motorright

                time.sleep(.01)
    except KeyboardInterrupt:
        scrollphat.clear()
        dw.allOff()
        sys.exit(-1)
