class Datagram:
	def __init__(self, content = 'Hello world', instructionContent = 0, datagramType = 0):
		self.datagramType = datagramType
		self.instructionContent = instructionContent
		self.content = content

	def GetType(self):
		return self.datagramType

	def SetType(self, datagramType):
		self.datagramType = datagramType

	def GetInstructionContent(self):
		return self.instructionContent

	def SetInstructionContent(self, instructionContent):
		self.instructionContent = instructionContent

	def GetContent(self):
		return self.content

	def SetContent(self, content):
		self.content = content