#!/usr/bin/env python3
#
# 2022-04-25 Tom Wizetek
#
# Install:
# python-pip
##
# python-rtmidi
# $ pip install -U novation-launchpad
#
# https://github.com/eavelardev/novation-launchpad
#
# or
##
# python-pygame
# $ pip install -U launchpad-py
#
# https://github.com/FMMT666/launchpad.py

import novation_launchpad as launchpad
#import launchpad_py as launchpad
from random import randint
from time import sleep
from signal import signal, SIGINT
from sys import exit

def main():

	#
	# Init
	#

	lp = launchpad.Launchpad()

	# Debug
	lp.ListAll()

	# lp.Open(), lp.Open(0), lp.Open( 0, "S"), lp.Open( 0, "Launchpad S")
	if lp.Open():
		print( "\nSuccess opening Launchpad" )
	else:
		print( "\nError opening Launchpad" )
		return

	# Forget all previously pressed buttons
	lp.ButtonFlush()

	# Reset all lights
	lp.Reset()

	#
	# Functions
	#

	def handler(signum, frame):
		lp.Reset()
		lp.Close()
		exit(0)

	def blink_all():
		for n in range(5):
			# LedAllOn(N) 0 = Turn all OFF, 1 = Turn all ON
			lp.LedAllOn(1)
			sleep(0.1)
			lp.LedAllOn(0)
			sleep(0.1)

	def all_red():

		# Range 9 = from 0 to 8 (0-7 squares + 1 row of ovals)
		# LedCtrlXY( self, x, y, red, green )

		for x in range(9):
			for y in range(9):
				lp.LedCtrlXY( x, y, 3, 0 )

	def all_green():
		for x in range(9):
			for y in range(9):
				lp.LedCtrlXY( x, y, 0, 3 )

	def all_yellow():
		for x in range(9):
			for y in range(9):
				lp.LedCtrlXY( x, y, 3, 3 )

	def blink(color=0, times=5, freq=0.1):

		# blink()	      	= yellow 5 times, 0.1s sleep between
		# blink("yellow")	= yellow x5
		# blink(4)		= yellow x4
		# blink("red", 3)	= red x3
		# blink("green", 2, 1)	= green x2 at 1s

		for n in range(times):

			if color == "red": all_red()
			elif color == "green": all_green()
			else: all_yellow()

			sleep(freq)
			lp.Reset()
			sleep(freq)

	def grow():
		# Loop length: 1000 x 0.1s = 10s
		for n in range(1000):

			# x: 0-7 = squares, 8 = ovals
			# y: 0 = ovals, 1-8 = squares

			x = randint(0, 8)
			y = randint(0, 8)
			
			while True:
				a = randint(0, 3)
				b = randint(0, 3)

				# Prevent 0,0 combo (light off)
				if a == b == 0: continue
				else: break

			lp.LedCtrlXY( x, y, a, b )
			sleep(0.01)

	def shift():
		# Loop length: 20 x 0.5s = 10s
		for n in range(20):
			for x in range(9):
				for y in range(9):

					while True:
						a = randint(0, 3)
						b = randint(0, 3)
						if a == b == 0: continue
						else: break

					lp.LedCtrlXY( x, y, a, b )
			sleep(0.5)

	def dissolve():
		# Squares only on X are range 0-7
		for x in range(8):
			lp.LedCtrlXY( x, 0, 0, 0 )
			sleep(0.1)

		for y in range(8):
			# y+1 here because squares on Y are range 1-8, not 0-7
			lp.LedCtrlXY( 8, y + 1, 0, 0 )
			sleep(0.1)

		# Loop length: 250 x 0.01s
		for n in range(250):
			x = randint(0, 8)
			y = randint(0, 8)
			lp.LedCtrlXY( x, y, 0, 0 )
			sleep(0.01)

	def wipe():
		# Red top-to-bottom left-to-right
		for y in range(9):
			for x in range(9):
				lp.LedCtrlXY( x, y, 3, 0 )
				sleep(0.004)

		# Yellow bottom-to-top right-to-left
		# Range from 8 to 0 step -1 non-inclusive (ends on 0, not -1)
		for y in range(8, -1, -1):
			for x in range(8, -1, -1):
				lp.LedCtrlXY( x, y, 3, 3 )
				sleep(0.004)

		# Green right-to-left top-to-bottom
		for x in range(8, -1, -1):
			for y in range(9):
				lp.LedCtrlXY( x, y, 0, 3 )
				sleep(0.004)

		# Off left-to-right top-to-bottom
		for x in range(9):
			for y in range(9):
				lp.LedCtrlXY( x, y, 0, 0 )
				sleep(0.004)

	#
	# MAIN LOOP
	#

	while True:

		signal(SIGINT, handler)

		blink("red")

		#
		# Single character
		#

		# LedCtrlChar( self, char, red, green, offsx = 0, offsy = 0 )

		# Red A
		lp.LedCtrlChar( "A", 3, 0 )
		sleep(1)

		blink("yellow")

		# Yellow B
		lp.LedCtrlChar( "B", 3, 3 )
		sleep(1)

		blink("green")

		# Green C
		lp.LedCtrlChar( "C", 0, 3 )
		sleep(1)

		# Strobe
		blink("yellow", 16, 0.03)

		#
		# Non-scrolling string
		#

		# LedCtrlString( self, string, red, green, direction = None, waitms = 150 )

		# Red, yellow, green ABC
		lp.LedCtrlString( "ABC ", 3, 0, 0, waitms = 100 )
		lp.LedCtrlString( "ABC ", 3, 3, 0, waitms = 100 )
		lp.LedCtrlString( "ABC ", 0, 3, 0, waitms = 100 )

		wipe()

		#
		# Scroller random color
		#

		# LedCtrlString( self, string, red, green, direction = None, waitms = 150 )

		a = randint(0, 3)

		# Do not allow off/low/medium light combos, i.e. 0,0 0,1 1,0 1,1 0,2 2,0 1,2 2,1 2,2
		if a <= 2: b = 3
		else: b = randint(0, 3)

		lp.LedCtrlString( "ABC A B C", a, b, -1, waitms = 75 )

		#
		# Random blips
		#

		grow()
		shift()
		dissolve()
		wipe()

if __name__ == '__main__':
	main()
##
