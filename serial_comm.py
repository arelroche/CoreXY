import serial
from time import sleep
from convert_gcode import convert_gcode as move
import main

def ser_init():
	ser=serial.Serial(port='\\.\COM7', baudrate=250000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	print(ser.name)
	return ser

def ser_arduino(ser):
	while True:
		print ser.read(1000)
		sleep(2)
		command = raw_input('Enter command:')
		if(command == 'home'):
			print "homing..."
			home(ser)
		elif(command == 'off'):
			print "turning motors off"
			off(ser)
		elif(command == 'on'):
			print "turning motors on"
			on(ser)
		elif(command == 'pick' or command == 'place'):
			col = raw_input("Enter column: ")
			row = raw_input("Enter row: ")
			print "performing a %s at %s%s" % (command, col, row)
			moveArray = []
			moveArray.append((command, col, row))
			move(ser, moveArray)
		elif (command == "auto"):
			main.computer_play(ser)
		else:
			print "Sending %s" % command
			ser_command(ser, command)
		
		sleep(2)

def ser_command(ser, command):
	ser.write(command + "\n")
	print ser.read(100)



	# print ser.read(10000)
	# print ser.write('M121')
	# print ser.read(1000)
	# print ser.write('G91')
	# print ser.read(1000)
	# print ser.write('G1 X100')
	# print ser.read(1000)

def home(ser):
	ser_command(ser,'G28 X0 Y0') #home
	moveArray = []
	col = "A"
	row = 11
	moveArray.append(("place", col, row))
	move(ser, moveArray)

def off(ser):
	ser_command(ser,'M18') #off
	ser_command(ser,'M107')

def on(ser):
	ser_command(ser,'M17') #on

	