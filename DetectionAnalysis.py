'''
Created on Jan 27, 2018

@author: rozita.teymourzadeh
'''
#import sys
import time
from _mysql import NULL
import csv
import math

#class DetectionAnalysis(object):	
#   def __init__(self,ref,target):		 
#		 self.ref = ref
#		 self.target = target		 
#		 data = open(path, "r")
#		 message = data.read()
#		 print(message)
#		 data.close()


# in , not in 

# to print time
def csv2list(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        lines = list(reader)
        list_data = []
        for values in lines:
            list_data.append(values)
    return list_data
        
        
def show_time(arg=NULL):
    arg = time.ctime();
    print(arg)

# to print header banner     
def banner(message,border='.'):
    line=border * len(message)
    print(line)
    print(message)
    print(line)
    
# To find Minimum/Maximum of file 
def minmax(items):
    return min(items),max(items)

# Analysis tool  
def __calculation__():
    state = []
    x_fw = []
    y_fw = []
    detection = open(r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_Detection.txt','r')
    #csv2list(r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_Detection.txt')
    #detection = open(target,'r')
    lines_fw = detection.readlines()
    detection.close()
    for line in lines_fw:
		line = line.strip()
		state =line.split(";")[2]
		x_fw = line.split(";")[3]
		y_fw = line.split(";")[4]
    print "state is {0} \n x_fw is {1} \n y_fw is {2}".format(state,x_fw,y_fw)

    min_x_fw_coordinate, max_x_fw_coordinate = minmax(x_fw)
    min_y_fw_coordinate, max_y_fw_coordinate = minmax(y_fw)
    print  "Minimum x_fw is:{0} \nMaximum x_fw is:{1}".format(min_x_fw_coordinate , max_x_fw_coordinate) 

		
    x_rob=[]
    y_rob=[]
    robot = open(r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_RobotPositions.txt','r')
    
    #robot=open(ref,'r')
    lines_robot = robot.readlines()
    robot.close()
    x_rob = line.split(";")[1]
    y_rob = line.split(";")[2]

    for line in lines_robot:
		line = line.strip()
		x_rob = line.split(";")[1]
		y_rob = line.split(";")[2]
    print "x_rob is {0} \ny_rob is {1} ".format(x_rob,y_rob)
        
def main():
    show_time() 
    banner("Analytical tool execution started...") 
    __calculation__()

	   	
if __name__ == '__main__':
	
	#main(sys.argv[1])
    #ref = "r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_Detection.txt'"
    #target = "r'C:\Users\Rozita.Teymourzadeh\Desktop\Accuracy\testData\RobotMeasurement_Detection.txt'"
    main()

 