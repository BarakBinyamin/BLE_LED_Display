import os
import serial
import time
import wx

#connect
os.system("./script2.sh")

ArrayString = ""
staticArray = []
tempArray = [25]
#off = wx.Image("LEDoff.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
#on = wx.Image("LEDon.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()

def NewArrayString():
		ArrayString = ""
		for element in tempArray:
			ArrayString = ArrayString + " " + str(element)

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		#& (wx.MINIMIZE_BOX) & (wx.CLOSE_BOX) & (wx.MAXIMIZE_BOX) --> to remove top bar
		wx.Frame.__init__(self, parent, title=title, size=(1000,900), style=wx.DEFAULT_FRAME_STYLE)
		self.Centre()

		p = wx.Panel(self) 
		gs = wx.GridSizer(5, 20, 20) #grid sizer

		icon = wx.Icon()
		icon.CopyFromBitmap(wx.Bitmap("LED.png", wx.BITMAP_TYPE_ANY))
		self.SetIcon(icon)

		x=70
		y=40
		self.Off_Buttons = []
		self.On_Buttons = []

		def Make_button(index):
			image = wx.Image("LEDoff.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			button = wx.BitmapButton(p, id=x, bitmap=image, size=(50, 50))
			gs.Add(button,0,wx.EXPAND) 
			temp_var = str(index) + "off"
			button.Bind(wx.EVT_BUTTON, lambda evt, temp=temp_var: self.OnClick(evt, temp) )
			button.temp = "off"
			self.Off_Buttons.append(button)
	
		for n in range(5):
			Make_button(n)
			print(n)

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx
		y+=180
		x=70
		for n in range(5, 10):
			Make_button(n)
			print(n)
			

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx
		y+=180
		x=70
		for n in range(10, 15):
			Make_button(n)
			print(n)

			dy = 1
			y += dy
			dx = 200
			x += dx
		y+=180
		x=70
		for n in range(15, 20):
			Make_button(n)
			print(n)

			dy = 1
			y += dy
			dx = 200
			x += dx
		y+=180
		x=70
		for n in range(20, 25):
			Make_button(n)
			print(n)

			dy = 1
			y += dy
			dx = 200
			x += dx
		p.SetSizer(gs) 
		self.Show(True)


	def OnClick(self, Event, additionalArgument):
		# ---
		def switch(string):
			switch_var = string
			if "off" in switch_var:
				switch_var = switch_var.replace('off','')
				switch_var = int(switch_var)
				self.button1Click(Event, switch_var)
				return switch_var
			if "on" in additionalArgument:
				switch_var = switch_var.replace('on','')
				switch_var = int(switch_var)
				self.button2Click(Event, switch_var)
				return switch_var
			return 0
		# ---
		arg = switch(additionalArgument)
		RowColumn = str(arg)
		print(RowColumn)
		command = "./write2.sh " + RowColumn
		tempArray.append(RowColumn)
		staticArray.append(RowColumn)
		os.system(command)


	def OnSave(self, Event, additionalArgument):
		RowColumn = str(additionalArgument)
		print(RowColumn)
		NewArrayString()
		tempArray=[]
		command = "./theWrite.sh"
		os.system(command)
	def OnPlay(self, Event, additionalArgument):
		RowColumn = str(additionalArgument)
		print(RowColumn)
		os.system(command)

	def button1Click(self,event, index):
		button=event.GetEventObject()
		if button.temp == "off":
			button.temp = "on"
			button.SetBitmap(wx.Bitmap('LEDon.png'))
		else:
			button.temp = "off"
			button.SetBitmap(wx.Bitmap('LEDoff.png'))


app = wx.App(False)
frame = MainWindow(None, "LED Display")
app.MainLoop()


