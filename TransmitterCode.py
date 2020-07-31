
import serial 
s = serial.Serial('COM5',9600)
#s.write()
s.write(open("strimg","rb").read())
s.close()


