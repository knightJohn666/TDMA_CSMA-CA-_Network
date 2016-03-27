from tkinter import *

class NodeSys:
	def __init__(self):
		window = Tk()
		window.title("Node")

		#Widget size
		LABEL_WIDTH = 20
		BUTTON_WIDTH = 15
		ENTRY_WIDTH = 20
		TEXT_WIDTH = 55
		TEXT_HIGHT = 10

		#Connection Frame
		connectionFrame = Frame(window)
		connectionFrame.grid(row = 1, column = 1, sticky = W)
		Label(connectionFrame, width = LABEL_WIDTH, text = "IP:").grid(row = 1, column = 1, sticky = W)
		self.ipValue = StringVar() 		#Self Value: ipValue(The value of the controller ip)
		Entry(connectionFrame, width = ENTRY_WIDTH, textvariable = self.ipValue).grid(row = 1, column = 2, sticky = W)
		self.ipValue.set("192.168.1.116")
		#Self Variable: connectionStateButton(The object of the connection state button)
		self.connectionStateButton = Button(connectionFrame, width = BUTTON_WIDTH, text = "Connect", command = self.ChangeConnectionStateProcess)
		self.connectionStateButton.grid(row = 1, column = 3, sticky = W)

		#MessageScreen Frame
		messageScreenFrame = Frame(window)
		messageScreenFrame.grid(row = 2, columnspan = 3, sticky = W)
		scrollbar = Scrollbar(messageScreenFrame)
		scrollbar.pack(side = RIGHT, fill = Y)
		#Self Object: messageScreen(To insert message to the screen)
		self.messageScreen = Text(messageScreenFrame, width = TEXT_WIDTH, height = TEXT_HIGHT, wrap = WORD, yscrollcommand = scrollbar.set)
		self.messageScreen.pack()
		self.messageScreen.insert(END, "Records As Follow:\n")

		#Message Frame
		messageFrame = Frame(window)
		messageFrame.grid(row = 3, column = 1, sticky = W)
		self.nodeNameLable = Label(messageFrame, width = LABEL_WIDTH, text = "NodeName:")
		self.nodeNameLable.grid(row = 1, column = 1, sticky = W)
		#Self Variable: messageValue(To get the content of the message)
		self.messageValue = StringVar()
		Entry(messageFrame, width = ENTRY_WIDTH, textvariable = self.messageValue).grid(row = 1, column = 2, sticky = W)
		Button(messageFrame, width = BUTTON_WIDTH, text = "Send", command = self.SendProcess).grid(row = 1, column = 3, sticky = W)

		#Average Delay Time Frame
		averageDelayTimeFrame = Frame(window)
		averageDelayTimeFrame.grid(row = 4, column = 1, sticky = W)
		Label(averageDelayTimeFrame, width = LABEL_WIDTH, text = "Average Delay:").grid(row = 1, column = 1, sticky = W)
		#Self Variable: averageDelayValue(To calculate the result of the average delay time)
		self.averageDelayValue = StringVar()
		Entry(averageDelayTimeFrame, width = ENTRY_WIDTH, textvariable = self.averageDelayValue).grid(row = 1, column = 2, sticky = W)

		#Current working state
		currentWorkingStateFrame = Frame(window)
		currentWorkingStateFrame.grid(row = 5, column = 1, columnspan = 3)
		self.currentWorkingStateValue = StringVar()		#Self Value: currentWorkingStateValue(The value of current working state)
		Message(currentWorkingStateFrame, textvariable = self.currentWorkingStateValue, justify = CENTER).grid(row = 1, column = 2, sticky = E)
		self.currentWorkingStateValue.set("Hello World")

		mainloop()

	def ChangeConnectionStateProcess(self):
		if( self.connectionStateButton["text"] == "Connect"):
			self.connectionStateButton["text"] = "Disconnect"
		else:
			self.connectionStateButton["text"] = "Connect"

	def SendProcess(self):
		print("SendProcess")

def main():
	NodeSys()

main()