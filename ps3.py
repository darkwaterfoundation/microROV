#!/usr/bin/env python
########################################################################                                               
# This is the library to read values from PS3 Dualshock 3 controller
#                                
# http://www.dexterindustries.com/GoPiGo/                                                                
# History
# ------------------------------------------------
# Author     	Date      		Comments
# Karan Nayan   11 July 14		Initial Authoring                                                   
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
#
# Dependencies- pygame
# Pairing the controller using bluetooth
# http://booting-rpi.blogspot.ro/2012/08/dualshock-3-and-raspberry-pi.html
# PS3 Key configuration http://wiki.ros.org/ps3joy
# 
# Key values can be obtained by creating a ps3 object and calling update() regularly
########################################################################
import pygame, sys, time ,os
from pygame.locals import *

# initialise pygame outside of the object so only done once
pygame.init()
screen = pygame.display.set_mode((1, 1), pygame.NOFRAME)
pygame.joystick.init()
#PS3 functions and variables
class ps3:
	#Initialize the controller when the oject is created
	def __init__(self):
		#Make the stdout buffer as 0,because of bug in Pygame which keeps on printing debug statements
		#http://stackoverflow.com/questions/107705/python-output-buffering
		#sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
		self.joystick_count = pygame.joystick.get_count()
                #set to -1 to enfoce a 0 setting on first pass
		self.lastleft = -1
		self.lastright = -1
		self.lastvert = -1
		self.lastvert2 = -1
		self.lastside = -1
		self.lastbuttontime = 0
		# get count of joysticks=1, axes=27, buttons=19 for DualShock 3
	def select_joystick(self, num):
		if num == 0:
			self.identifier = "aa"
		elif num == 1:
			self.identifier = "ab"
		self.joysticknum = num
		self.joystick = pygame.joystick.Joystick(num)
		self.joystick.init()
		self.numaxes = self.joystick.get_numaxes()
		self.numbuttons = self.joystick.get_numbuttons()
	#Update the button values
	def update(self):
		loopQuit = False
		button_state=[0]*self.numbuttons
		button_analog=[0]*self.numaxes
		#while loopQuit == False:
		outstr = ""
		
		#Start suppressing the output on stdout from Pygame
		#devnull = open('/dev/null', 'w')
		#oldstdout_fno = os.dup(sys.stdout.fileno())
		#os.dup2(devnull.fileno(), 1)
		
		#Read analog values
		for i in range(0,self.numaxes):
			button_analog[i] = self.joystick.get_axis(i)
		
		#a_left				=button_analog[]
		self.a_right				=button_analog[9]
		self.a_up				=button_analog[8]
		self.a_down				=button_analog[10]
		self.a_l1				=button_analog[14]
		self.a_l2				=button_analog[12]
		self.a_r1				=button_analog[15]
		self.a_r2				=button_analog[13]
		self.a_triangle			=button_analog[16]
		self.a_circle			=button_analog[17]
		self.a_square			=button_analog[19]
		self.a_cross				=button_analog[18]

		self.a_joystick_left_x	=button_analog[0]
		self.a_joystick_left_y	=button_analog[1]
		self.a_joystick_right_x	=button_analog[2]
		self.a_joystick_right_y	=button_analog[3]
		self.acc_x				=button_analog[23]
		self.acc_y				=button_analog[24]
		self.acc_z				=button_analog[25]
		
		#Read digital values
		for i in range(0,self.numbuttons):
			button_state[i]=self.joystick.get_button(i)
		self.select			=button_state[0]
		self.joystick_left	=button_state[1]
		self.joystick_right	=button_state[2]
		self.start			=button_state[3]
		self.up				=button_state[4]
		self.right			=button_state[5]
		self.down			=button_state[6]
		self.left			=button_state[7]
		self.l2				=button_state[8]
		self.r2				=button_state[9]
		self.l1				=button_state[10]
		self.r1				=button_state[11]
		self.triangle		=button_state[12]
		self.circle			=button_state[13]
		self.cross			=button_state[14]
		self.square			=button_state[15]
		self.ps				=button_state[16]
		
		#Enable output on stdout
		#os.dup2(oldstdout_fno, 1)	
		#os.close(oldstdout_fno)
		
		#refresh
		pygame.event.get()
		return button_analog
	
