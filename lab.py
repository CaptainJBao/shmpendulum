import csv
import numpy as np
import matplotlib.pyplot as plot
import math

dataList = []

def importData (fileName):
    with open(fileName) as rawData:
        dataAnalyze = csv.reader(rawData)
        for row in dataAnalyze:
            dataList.append(row)

def exportData (fileName):
    dataList[0] = ["Trial", "Start", "Finish", "Period"]
    with open(fileName, 'w') as final:
        dataWrite = csv.writer(final)
        for data in dataList:
            dataWrite.writerow(data)

def calcPeriod ():
    period = 0.0
    for i in range(1,len(dataList)):
        dataList[i].append(str(float(dataList[i][2]) - float(dataList[i][1])))
        period += float(dataList[i][3])
    return period / (len(dataList) - 1)

def calcOmega (length):
    return math.sqrt(9.8/length)

def calcAmplitude (theta, length):
    return length * theta * math.pi / 180

def calcPeriodTheoretical (length):
    return 2 * math.pi * math.sqrt(length / 9.8)

def sinegraph (amplitude, omega,name,ylabel,phase):
    x = np.arange(0, 35, 0.1)
    y = amplitude * np.sin(omega * x + phase)
    graph(x,y,name,ylabel)

def cosinegraph (amplitude, omega,name,ylabel):
    x = np.arange(0, 35, 0.1)
    y = amplitude * np.cos(omega * x)
    graph(x,y,name,ylabel)

def graph (x,y,name,ylabel):
    plot.plot (x, y)
    plot.title (name)
    plot.xlabel ("Time (s)")
    plot.ylabel (ylabel)
    plot.grid (True, which = 'both')
    plot.axhline (y = 0, color = 'k')
    plot.show()

def equation (fileName, length, theta):
    sinx = "Sine graph of the pendulum's position vs. time"
    cosx = "Cosine graph of the pendulum's position vs. time"
    pos = "Position (m)"
    vel = "Velocity (m/s)"
    acc = "Acceleration (m/s^2)"
    velocityName = "Graph of the pendulum's velocity vs. time"
    accelerationName = "Graph of the pendulum's acceletation vs. time"
    importData (fileName)
    amplitude = round(calcAmplitude(theta,length), 3)
    omega = round(calcOmega(length),3)
    print ("cosine equation for x(t): ",amplitude, "cos(",omega, "t)",sep = "")
    print ("sine equation for x(t): ",amplitude, "sin(",omega, "t+pi/2)",sep = "")
    print ("equation for the velocity vs. time function: ", round(amplitude * omega * -1,3), "sin(",omega, "t)",sep = "")
    print ("equation for the acceleration vs. time function: ", round(amplitude * (omega**2) * -1,3), "cos(",omega, "t)",sep = "")
    print ("Theoretical value for period:", round(calcPeriodTheoretical(length),3))
    print ("Experimental value for period:", round(calcPeriod(),3))
    cosinegraph (amplitude, omega, cosx,pos)
    sinegraph (amplitude, omega,sinx,pos,(math.pi/2))
    sinegraph (amplitude * omega * -1, omega, velocityName,vel,0)
    cosinegraph ((amplitude * (omega**2) * -1), omega, accelerationName,acc)
    exportData (fileName)


equation ("experiment.csv", 0.55, 10)
