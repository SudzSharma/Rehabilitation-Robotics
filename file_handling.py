

import time
#Open a file
fo = open("m_data.txt", "r+")

print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

j=0
data=""
i=0
motor_data=[]
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
while True:


    chunk = fo.readline()
    if chunk == '':
        break
    else :
		#print "Data is :",chunk
		for j in range(0,len(chunk)):
			
			if(chunk[j]==','):
				motor_data[i]=float(data)
				data=""
				i=i+1
				if(i==5):
					break
			else:
				data=data+chunk[j]	

			#print "D",chunk[j]

	 	print "Motor_Data1",motor_data[0]
	 	print "Motor_Data2",motor_data[1]
		print "Motor_Data3",motor_data[2]
		print "Motor_Data4",motor_data[3]
		print "Motor_Data4",motor_data[4]
		print "Time",time.clock()
		i=0

		




