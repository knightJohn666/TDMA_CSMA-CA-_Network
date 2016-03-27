"import D:\\A课程\\A物联网\\lab2_network\\B代码\\Entity\\"

from NodeControl import *
from Entity.CommunicationUnit import *
from Entity.Token import *
from Entity.Datagram import *

class NodeCommunicationThread:
	def __init__(self):
		 self.nodeControl = NodeControl()
		 self.communicationUnit = CommunicationUnit()
		 