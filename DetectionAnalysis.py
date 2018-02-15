'''
Created on Jan 27, 2018

@author: rozita.teymourzadeh
'''
import sys
import time

#class DetectionAnalysis(object):	
#   def __init__(self,ref,target):		 
#		 self.ref = ref
#		 self.target = target		 
#		 data = open(path, "r")
#		 message = data.read()
#		 print(message)
#		 data.close()

def show_default(arg=time.ctime()):
    print(arg)
    
def banner(message,border='_'):
    line=border * len(message)
    print(line)
    print(message)
    print(line)
    
def __calculation__(ref,target):
    state=[]
    x_fw=[]
    y_fw=[]
#		detection = open(r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_Detection.txt','r')
    detection = open(target,"r")
    lines_fw = detection.readlines()
    detection.close()
    for line in lines_fw:
		line = line.strip()
		state = line.split(";")[2]
		x_fw = line.split(";")[3]
		y_fw = line.split(";")[4]
		print ( "state: ",state,"x_fw: ",x_fw,"y_fw: ", y_fw )
		
    x_rob=[]
    y_rob=[]
#		robot = open(r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_RobotPositions.txt','r')
    robot=open(ref)
    lines_robot = robot.readlines()
    robot.close()
    for line in lines_robot:
		line = line.strip()
		x_rob = line.split(";")[1]
		y_rob = line.split(";")[2]
		print ("x_rob: ","y_rob: ", x_rob,y_rob)
def main(ref,target): 
	   #DetectionAnalysis(ref,target)
#	   __init__(ref,target)
    __calculation__(ref,target)	
	   	
if __name__ == '__main__':
	
	main(sys.argv[1],sys.argv[2])

 