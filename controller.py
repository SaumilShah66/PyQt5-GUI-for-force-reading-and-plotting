###################################################################
######## Made for mototr controller using arduino #################
###################################################################
import serial
import serial.tools.list_ports
from numpy import pi
from errors import show_error

class motor_controller():
	def __init__(self):
		self.controller_manu = "Arduino LLC (www.arduino.cc)"	 # Controller manufacturer
		self.found = False
		self.com = None
		self.controller_connected = False
		self.errors_ = show_error()

	def find_com(self):                             		# This function finds the com port where arduino is connected  using manufacturer
		comlist = serial.tools.list_ports.comports()      	# gives list of active COM ports
		connected = []
		for element in comlist:
			connected.append(element)
		for connection in connected:
			if connection.manufacturer == self.controller_manu:
				self.com = connection.device                     # COM port where mark 10 is connected
				self.found = True 

	def connect_com(self):                                        ### This function returns controller connected object
		self.find_com()
		if self.found:                                          # checking flag
			try:
				self.s = serial.Serial(self.com, 9800)
				print("Controller is connected successfully")
				self.controller_connected = True
				return True                                       
			except:
				print("Umable to connect controller")
				self.errors_.controller_connection_problem()
				return False
		else:
			print("Didn't found controller")
			self.errors_.controller_not_found()
			return False

	def rotate_axis_signal(self, speed, distance):
		stpPrev = 51200
		roller_dia = 25
		steps = int(stpPrev*abs(distance)/(pi*roller_dia))
		time = floa(abs(distance))/speed
		tps = int(float(time*(10**6))/float(steps))
		###########################################################################################
		################ Format of command is ---- axis/roller,number of steps,delay time #########
		###########################################################################################
		command = 'a,'+str(tps)+","+str(steps)+","+str(distance/abs(distance))
		if self.controller_connected:
			self.s.write(command.encode('utf-8'))
			if self.s.in_waiting>0:
				print(self.s.read(self.s.in_waiting))
			else:
				pass
		else:
			print("Controller is not connected")
			self.errors_.cannot_move_motor()

	def rotate_roller_signal(self, speed, distance):
		stpPrev = 51200
		roller_dia = 25
		steps = int(stpPrev*abs(distance)/(pi*roller_dia))
		time = float(abs(distance))/speed
		tps = int(float(time*(10**6))/float(steps))
		command = 'r,'+str(tps)+","+str(round(time*1000))+","+str(distance/abs(distance))
		print(command)
		if self.controller_connected:
			self.s.write(command.encode('utf-8'))
			if self.s.in_waiting>0:
				print(self.s.read(self.s.in_waiting))
			else:
				pass
		else:
			print("Controller is not connected")
			self.errors_.cannot_move_motor()

	def rotate_axis_one_left(self):
		if self.controller_connected:
			command = 'a,10,51200,-1'
			self.s.write(command.encode('utf-8'))
			if self.s.in_waiting>0:
				print(self.s.read(self.s.in_waiting))
			else:
				pass
		else:
			print("Controller is not connected")
			self.errors_.cannot_move_motor()

	def rotate_axis_one_right(self):
		if self.controller_connected:
			command = 'a,10,51200,1'
			self.s.write(command.encode('utf-8'))
			if self.s.in_waiting>0:
				print(self.s.read(self.s.in_waiting))
			else:
				pass
		else:
			print("Controller is not connected")
			self.errors_.cannot_move_motor()

	def stop(self):
		self.s.close()
		print("Disconnected successfully")