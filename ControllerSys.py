from tkinter import *

class ControllerSys:
	def __init__(self):
			window = Tk()
			window.title("Controller")

			#Widget Size
			LABEL_WIDTH = 25
			ENTRY_WIDTH = 15
			BUTTON_WIDHT = 20

			#WorkMode Frame
			workModeFrame = Frame(window)
			workModeFrame.grid(row = 1, column = 1, sticky = W)
			Button(workModeFrame, width = BUTTON_WIDHT, text = "TDMA WorkMode", command = self.TDMAProcess).grid(row = 1, column = 1)
			Button(workModeFrame, width = BUTTON_WIDHT, text = "CSMA_CA WorkMode", command = self.CSMA_CAProcess).grid(row = 1, column = 2)

			#Time slot Frame
			timeSlotFrame = Frame(window)
			timeSlotFrame.grid(row = 2, column = 1, sticky = W)
			Label(timeSlotFrame, width = LABEL_WIDTH, text = "Duration:").grid(row = 1, column = 1)
			self.durationValue = StringVar()	#Self Value: durationValue(The size of time slot of the TDMA workMode)
			Entry(timeSlotFrame, width = ENTRY_WIDTH, textvariable = self.durationValue, justify = LEFT).grid(row = 1, column = 2)

			#Node Frame
			nodeFrame = Frame(window)
			nodeFrame.grid(row = 3, column = 1, sticky = W)
			Label(nodeFrame, width = LABEL_WIDTH, text = "Number of current node:").grid(row = 1, column = 1, sticky = W)
			self.numberOfCurNodeValue = StringVar()	#Self Value: numberOfCurNodeValue(The number of current node)
			Entry(nodeFrame, width = ENTRY_WIDTH, textvariable = self.numberOfCurNodeValue, justify = LEFT).grid(row = 1, column = 2, sticky = E)

			#Channel Efficiency Frame
			channelEfficiencyFrame = Frame(window)
			channelEfficiencyFrame.grid(row = 4, column = 1, sticky = W)
			Label(channelEfficiencyFrame, width = LABEL_WIDTH, text = "Channel Efficiency:").grid(row = 1, column = 1, sticky = W)
			self.channelEfficiencyValue = StringVar()	#Self Value: channelEfficiencyValue(The value of channel efficiency)
			Entry(channelEfficiencyFrame, width = ENTRY_WIDTH, textvariable = self.channelEfficiencyValue, justify = LEFT).grid(row = 1, column = 2, sticky = E)

			#Throughout Frame
			throughoutFrame = Frame(window)
			throughoutFrame.grid(row = 5, column = 1, sticky = W)
			Label(throughoutFrame, width = LABEL_WIDTH, text = "Throughout:").grid(row = 1, column = 1, sticky = W)
			self.throughoutValue = StringVar() 	#Self Value: throughoutValue(The value of throughout)
			Entry(throughoutFrame, width = ENTRY_WIDTH, textvariable = self.throughoutValue, justify = LEFT).grid(row = 1, column = 2, sticky = E)

			#Current working state
			currentWorkingStateFrame = Frame(window)
			currentWorkingStateFrame.grid(row = 6, column = 1, sticky = S)
			self.currentWorkingStateValue = StringVar()		#Self Value: currentWorkingStateValue(The value of current working state)
			Message(currentWorkingStateFrame, textvariable = self.currentWorkingStateValue).grid(row = 1, column = 1, sticky = S)
			self.currentWorkingStateValue.set("Hello world")

			mainloop()

	def TDMAProcess(self):
		print("TDMAProcess")

	def CSMA_CAProcess(self):
		print("CSMA_CAProcess")

def main():
	ControllerSys()

main()