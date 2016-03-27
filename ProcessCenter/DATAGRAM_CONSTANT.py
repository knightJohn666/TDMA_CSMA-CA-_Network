class DATAGRAM_CONSTANT:
	def __init__(self):
		self.NODE_OPERATION = 0		#0结点报文
		self.DELETE_NODE = 0			#1删除结点
		self.CREATE_NODE = 1			#1新建结点

		self.SEND_OPERATION = 1		#1发送报文
		self.SEND_FINISHED = 0		#0发送完毕
		self.SEND_READY = 1			#1发送请求

		self.WORKMODE_OPERATION = 2		#2工作模式
		self.COLLISION_AVOIDING = 0		#0冲突避免模式
		self.TIME_SLOT = 1				#1轮询模式

		self.DATA_OPERATION = 3		#3数据报文
		
		
		
