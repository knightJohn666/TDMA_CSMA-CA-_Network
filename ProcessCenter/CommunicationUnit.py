import socket
import sys
import time
from Entity.Datagram import *
from Entity.Token import *
from ProcessCenter.MyJson import *

class CommunicationUnit:
	def __init__(self):
		self.workingState = False

	def InitSocket(self):
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Initialize the socket failed! Error is " + str(ErrorValue))
			return False

		print("Initialize successfully!")
		return True

	def Connect(self, IP):
		if not self.IsStr(IP) or self.IsNone(IP):
			return False

		try:
			self.socket.connect((IP, 8001))
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Connect failed! Error is " + str(ErrorValue))
			return False

		print("Connect successfully!")
		return True

	def Disconnect(self):
		try:
			self.socket.close()
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Disconnect failed! Error is " + str(ErrorValue))
			return False

		print("Disconnect successfully!")
		return True

	def Listen(self):
		try:
			self.socket.bind(('localhost', 8001))
			self.socket.listen(5)
			self.connection, self.address = self.socket.accept()
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Listen port failed! Error is " + str(ErrorValue))
			return False

		print("One connection is listened! Connection builds successfully!")
		return True

	def ServerSend(self, datagram):
		try:
			data = MyEncoder().encode(datagram)
			self.connection.send(data.encode("utf-8"))
			time.sleep(0.01)
			print(data.encode("utf-8"))
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Send failed! Error is " + str(ErrorValue))
			return False

		print("Send successfully!")
		return True

	def ServerReceive(self):
		try:
			data = self.connection.recv(1024)
			dataStr = data.decode()
			print(dataStr)
			datagram = MyDecoder().decode(dataStr)
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Receive failed! Error is " + str(ErrorValue))
			return None

		print("Receive datagram")
		return datagram

	def ClientSend(self, datagram):
		try:
			data = MyEncoder().encode(datagram)
			self.socket.send(data.encode("utf-8"))
			time.sleep(0.01)
			print(data.encode("utf-8"))
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Send failed! Error is " + str(ErrorValue))
			return False

		print("Send successfully!")
		return True

	def ClientReceive(self):
		try:
			data = self.socket.recv(1024)
			dataStr = data.decode()
			print(dataStr)
			datagram = MyDecoder().decode(dataStr)
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print("Receive failed! Error is " + str(ErrorValue))
			return None

		print("Receive datagram")
		return datagram

	def GetWorkingState(self):
		return self.workingState

	def SetWorkingState(self, workingState):
		self.workingState = workingState


	#Tool function
	#Check the object is none or not.
	def IsNone(self, value):
		if value == '':
			print("The node name is null, please input it again.")
			return True
		else:
			return False

	#Check the object's type is str or not.
	def IsStr(self, value):
		if isinstance(value, str):
			return True
		else:
			print("The type of " + str(value) + " unmatched with str")
			return False