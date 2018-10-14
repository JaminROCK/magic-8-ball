import random
import time
import sys
import tkinter as tk
def clicked(event):
	canvas.delete(canvas.gettags("inner"))
	canvas.delete(canvas.gettags("triangle"))
	canvas.delete(canvas.gettags("response"))
	window.after(150, barely)
	window.after(250, semi)
	window.after(350, almost)
	window.after(450, response)
	
def barely():
	canvas.delete(canvas.gettags("inner"))
	#inner circle
	canvas.create_oval(500,200, w-10, h-210, fill="#1b1b1c", tag="inner")
	#Pack, start loops
	print("semi")
def semi():
	canvas.delete(canvas.gettags("inner"))
	#inner circle
	canvas.create_oval(250,180, w-70, h-180, fill="#1b1b1c", tag="inner")
	#Pack, start loops
	print("semi")
def almost():
	canvas.delete(canvas.gettags("inner"))
	#inner circle
	canvas.create_oval(230,180, w-120, h-180, fill="#1b1b1c", tag="inner")
	#Pack, start loops
	print("semi")
def response():
	canvas.delete(canvas.gettags("inner"))
	#inner circle
	canvas.create_oval(180,180, w-180, h-180, fill="#1b1b1c", tag="inner")
	#Make Triangle
	points = [225, 255, 375, 255, 300, 375]
	canvas.create_polygon(points,fill="blue", tag="triangle")
	# generate random response
	r = random.randint(0,(len(lst)-1))
	response = lst[r]
	canvas.delete(canvas.gettags("response"))
	canvas.create_text(300,300,fill="white",font="Calibri 7 bold italic", text=response, tag="response")
	#Pack, start loops
	canvas.pack()
	# window.after(1000, response)
#define application and allow passingg cmd line args
window = tk.Tk()
#create window with modified starting position
window.title("Magic 8 Ball")
# Create list of responses
lst = []
#response list
lst.extend([" It is certain.",
			"It is decidedly\n          so.",
			"Without\na doubt.",
			"       Yes,\n  definitely.",
			"  You may\n  rely on it.",
			" As I see it,\n       yes.",
			" Most likely.",
			" Outlook good.",
			"    Yes.",
			"  Signs point\n      to yes.",
			"  Reply hazy,\n   try again.",
			"   Ask again\n      later.",
			"   Better not\ntell you now.",
			" Cannot predict\n          now.",
			" Concentrate\n         and\n    ask again.",
			"  Don't count\n        on it.",
			" My reply is no.",
			"  My sources\n     say no.",
			" Outlook not so\n         good.",
			" Very doubtful.",
			"Duh."])
#Place window in middle
w = 600 # width for the Tk root
h = 600 # height for the Tk root
# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#make canvas object
canvas = tk.Canvas(window, width = w, height = h, bg='#c2d1ea', highlightbackground="#c2d1ea")
#Make Eighball
canvas.create_oval(10,10, w-10, h-10, fill="black")
canvas.pack()
canvas.bind("<Button-1>", clicked)
# almost()
# response()
# canvas.create_text(200,200,fill="white",font="Calibri 5 bold", text=lst[15], tag="response")
window.mainloop()