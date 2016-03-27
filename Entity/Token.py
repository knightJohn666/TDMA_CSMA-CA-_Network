from Entity.Datagram import *

class Token(Datagram):
	def __init__(self, content = 'Hello world', instructionContent = 0, datagramType = 0, duration = 100, nodeName = "NodeName"):
		super().__init__(content, instructionContent, datagramType)
		self.duration = duration
		self.nodeName = nodeName

	def GetDuration(self):
		return self.duration

	def SetDuration(self, duration):
		self.duration = duration

	def GetNodeName(self):
		return self.nodeName

	def SetNodeName(self, nodeName):
		self.nodeName = nodeName