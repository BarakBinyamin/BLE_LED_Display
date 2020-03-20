import os
import serial
import time
import wx

#connect
os.system("./script2.sh")

ArrayString = ""
staticArray = []
tempArray = [25]

def NewArrayString():
		ArrayString = ""
		for element in tempArray:
			ArrayString = ArrayString + " " + str(element)

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(1000,900), style=wx.DEFAULT_FRAME_STYLE & (wx.MINIMIZE_BOX) & (wx.CLOSE_BOX) & (wx.MAXIMIZE_BOX))
		self.Centre()

		'''button = wx.Button(self, id=0,  size=(200, 50), pos=(20, 20))
		button.Bind(wx.EVT_BUTTON, lambda evt, temp="nope": self.OnSave(evt, temp) )
		button = wx.Button(self, id=1,  size=(200, 50), pos=(280, 20))
		button.Bind(wx.EVT_BUTTON, lambda evt, temp="nope": self.OnPlay(evt, temp) )'''
		x=70
		y=40
		self.Off_Buttons = []
		self.On_Buttons = []

		def Make_button(index):
			image = wx.Image("LEDoff.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			button = wx.BitmapButton(self, id=x, bitmap=image, size=(50, 50), pos=(x, y))
			temp_var = str(index) + "off"
			button.Bind(wx.EVT_BUTTON, lambda evt, temp=temp_var: self.OnClick(evt, temp) )
			image2 = wx.Image("LEDon.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			button2 = wx.BitmapButton(self, id=x, bitmap=image2, size=(50, 50), pos=(x, y))
			temp_var = str(index) + "on"
			button2.Bind(wx.EVT_BUTTON, lambda evt, temp=temp_var: self.OnClick(evt, temp) )
			self.Off_Buttons.append(button)
			self.On_Buttons.append(button2)
			button2.Hide()
	
		for n in range(5):
			#button = wx.Button(self, id=x,  size=(50, 50), pos=(x, y))
			#button.Bind(wx.EVT_BUTTON, lambda evt, temp=n: self.OnClick(evt, temp) )
			Make_button(n)
			print(n)

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx
		y+=180
		x=70
		for n in range(5, 10):
			#button = wx.Button(self, id=x,  size=(50, 50), pos=(x, y))
			#button.Bind(wx.EVT_BUTTON, lambda evt, temp=n: self.OnClick(evt, temp) )
			Make_button(n)
			print(n)
			

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx
		y+=180
		x=70
		for n in range(10, 15):
			#button = wx.Button(self, id=x,  size=(50, 50), pos=(x, y))
			#button.Bind(wx.EVT_BUTTON, lambda evt, temp=n: self.OnClick(evt, temp) )
			Make_button(n)
			print(n)

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx
		y+=180
		x=70
		for n in range(15, 20):
			#button = wx.Button(self, id=x,  size=(50, 50), pos=(x, y))
			#button.Bind(wx.EVT_BUTTON, lambda evt, temp=n: self.OnClick(evt, temp) )
			Make_button(n)
			print(n)

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx
		y+=180
		x=70
		for n in range(20, 25):
			#button = wx.Button(self, id=x,  size=(50, 50), pos=(x, y))
			#button.Bind(wx.EVT_BUTTON, lambda evt, temp=n: self.OnClick(evt, temp) )
			Make_button(n)
			print(n)

			dy = 1	 # calculate for next loop
			y += dy
			dx = 200 # calculate for next loop
			x += dx

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
		self.Off_Buttons[index].Hide()
		self.SetTitle("Button1 clicked")
		self.On_Buttons[index].Show()
	
	def button2Click(self,event, index):
		self.On_Buttons[index].Hide()
		self.SetTitle("Button2 clicked")
		self.Off_Buttons[index].Show()


app = wx.App(False)
frame = MainWindow(None, "MAIN")
app.MainLoop()
