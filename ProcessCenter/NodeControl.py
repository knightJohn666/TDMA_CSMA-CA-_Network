"import D:\\A课程\\A物联网\\lab2_network\\B代码\\Entity\\"

from Entity.Node import *

class NodeControl:
	def __init__(self):
		self.nodeList = []
		self.nodeMaxId = 0

		self.currentPosition = 0	#For implementing a loop list, which we can use nextNode function to transmit the list one by one

	def CreateNode(self):
		newNode = Node()
		newNode.SetNodeName("Node" + str(self.nodeMaxId))
		newNode.SetNodeId(self.nodeMaxId)
		self.nodeList.append(newNode)

		self.nodeMaxId += 1

		return newNode.GetNodeName()

	def DeleteNodeByName(self, nodeName):
		if (not self.IsStr(nodeName)) or self.IsNone(nodeName) or self.IsEmpty():
			return False

		node = self.GetNodeByName(nodeName)

		if(self.RemoveNode(node)):
			print(nodeName + " is removed successfully! ")
			return True
		else:
			print(nodeName + " is failed to remove! ")
			return False
		

	def DeleteNodeById(self, nodeId):
		if (not self.IsInt(nodeId)) or self.IsEmpty():
			return False

		node = self.GetNodeById(nodeId)

		if(self.RemoveNode(node)):
			print("The nodeId = " + str(nodeId) + " is removed successfully! ")
			return True
		else:
			print("The nodeId = " + str(nodeId) + " is failed to remove! ")
			return False

	def GetNextNode(self):
		if not self.IsEmpty():
			currentPosition = self.currentPosition % len(self.nodeList)
			self.currentPosition += 1
			return self.nodeList[currentPosition]

		return None

	#Get node object by nodeName
	def GetNodeByName(self, nodeName):
		if (not self.IsStr(nodeName)) or self.IsNone(nodeName) or self.IsEmpty():
			return None

		aimNode = None
		for node in self.nodeList:
			if node.nodeName == nodeName:
				aimNode = node
				break

		if(aimNode == None):
			print(nodeName + " doesn't exist")

		return aimNode

	#Get node object by nodeId
	def GetNodeById(self, nodeId):
		if (not self.IsInt(nodeId)) or self.IsEmpty():
			return None

		aimNode = None
		for node in self.nodeList:
			if node.nodeId == nodeId:
				aimNode = node
				break

		if(aimNode == None):
			print("The nodeId = " + str(nodeId) + " doesn't exist, please check it one more time")

		return aimNode

	#Get the total number of node
	def GetTotalNumberOfNode(self):
		return len(self.nodeList)

	#Modify node name
	def ModifyNodeName(self, oldNodeName, newNodeName):
		#oldNodeName是否合法
		if (not isinstance(oldNodeName, str)) or self.IsNone(oldNodeName) or self.IsEmpty():
			return False

		#newNodeName是否合法
		if (not isinstance(newNodeName, str)) or self.IsNone(newNodeName):
			return False

		#是否重名
		newNode = self.GetNodeByName(newNodeName)
		if newNode != None:
			print("The " + newNodeName + " has already existed! ")
			return False

		#修改名称
		oldNode = self.GetNodeByName(oldNodeName)
		if oldNode != None:
			oldNode.SetNodeName(newNodeName)
			print("Modify successfully!")
			return True

		return False



	#Tool functions
	#Check the nodeList is empty or not.
	def IsEmpty(self):
		if len(self.nodeList) <= 0:
			print("The node list is null")
			return True
		else:
			return False

	#Check the object is none or not.
	def IsNone(self, value):
		if value == '':
			print("The node name is null, please input it again.")
			return True
		else:
			return False

	#Check the node is exist or not.
	def IsNodeExist(self, node):
		if not IsNode(node):
			return -1

		nodePosition = 0
		for tempNode in self.nodeList:
			if tempNode.GetNodeName() == node.GetNodeName():
				break
			nodePosition += 1

		if nodePosition < len(self.nodeList):
			return nodePosition
		else:
			print("The nodeList doesn't contain " + node.GetNodeName())
			return -1

	#Check the node name is exist or not.
	def IsNodeNameExist(self, nodeName):
		if self.IsStr(nodeName) and self.IsNone(nodeName) and self.IsEmpty():
			return -2

		node = Node()
		node.SetNodeName(nodeName)

		nodePosition = self.IsNodeExist(node)
		if nodePosition == -1:
			return -1
		else:
			return nodePosition


	#Check the object's type is str or not.
	def IsStr(self, value):
		if isinstance(value, str):
			return True
		else:
			print("The type of " + str(value) + " unmatched with str")
			return False

	#Check the object's type is int or not.
	def IsInt(self, value):
		if isinstance(value, int):
			return True
		else:
			print("The type of " + str(value) + " unmatched with int")
			return False

	#Check the object's type is Node or not.
	def IsNode(self, value):
		if isinstance(value , Node):
			return True
		else:
			print("The type of " + str(value) + "unmatched with Node")
			return False

	#Remove node that has already existed in nodeList
	def RemoveNode(self, node):
		if node != None:
			self.nodeList.remove(node)
			return True
		else:
			return False