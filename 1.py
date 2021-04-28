from tkinter import *

from serial import Serial
import sys
import time

arduino = Serial('COM12', 9600, timeout =1)
def prepare_coomand(*args):
	
	b = args[0] + 48;
	arduino.write(b.to_bytes(length=1, byteorder='big', signed=False))

def serial_print():
	recive = str(arduino.readline())
	t = ("b'", "\\r\\n'", "\\n'")

	for i in t:
		recive = recive.replace(i, '')
		
	l = recive.split('\\t')

	if len(l) > 1:
		for i in l:
			print(i, end = "\t")
		print()
	else:
		print(l[0])
	


root = Tk()
def f():
	print("еду_вперед")
	b =  49;
	arduino.write(b.to_bytes(length=1, byteorder='big', signed=False))
	serial_print()

def r():
	print("еду_назад")
	b =  50;
	arduino.write(b.to_bytes(length=1, byteorder='big', signed=False))
	serial_print()

def p():
	print("поворачиваю_вправо")
	b =  51;
	arduino.write(b.to_bytes(length=1, byteorder='big', signed=False))
	serial_print()

def l():
	print("поворачиваю_влево")
	b =  52;
	arduino.write(b.to_bytes(length=1, byteorder='big', signed=False))
	serial_print()


b = Button(root, text = "вперед", command=f)

b.bind('<Button-1>')

b.grid(column = 2, row = 1)



b2 = Button(root, text = "право", command=p)

b2.bind('<Button-2>')

b2.grid(column = 3, row = 2)



b3 = Button(root, text = "назад", command=r)

b3.bind('<Button-3>')

b3.grid(column = 2, row = 2)



b4 = Button(root, text = "лево", command=l)

b4.bind('<Button-4>')

b4.grid(column = 1, row = 2)

root.mainloop()



