import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import serial

seru = serial.Serial('COM6', 115200)
x = []
y = []
z = []
fig = plt.figure()
def update_lines(num):
    #calling sensor function
    rmsX,rmsY,rmsZ = vib_sense()
    #Creating Numpy array and appending the values
    vib_x= np.array(rmsX)
    x.append(vib_x)
    vib_y= np.array(rmsY)
    y.append(vib_y)
    vib_z= np.array(rmsZ)
    z.append(vib_z)
    print(x)
    print(y)
    print(z)
    ax = fig.add_subplot(111, projection='3d')
    ax.clear()
    #Limit the Graph
    ax.set_xlim3d(0, 100)
    ax.set_ylim3d(0, 100)
    ax.set_zlim3d(0, 100)
    #for line graph
    graph = ax.plot3D(x,y,z,color='orange',marker='o')
    #For Scatter
    # graph = ax.scatter3D(x,y,z,color='orange',marker='o')
    return graph

def vib_sense():
    while True:
        s = seru.read(54)
        if(s[0] == 126):
            if(s[15] == 127):
                if(s[22]== 8):
                    rms_x = ((s[24]*65536)+(s[25]*256)+s[26])/1000
                    rms_y = ((s[27]*65536)+(s[28]*256)+s[29])/1000
                    rms_z = ((s[30]*65536)+(s[31]*256)+s[32])/1000
                    '''    
                    max_x = ((s[33]*65536)+(s[34]*256)+s[35])/1000
                    max_y = ((s[36]*65536)+(s[37]*256)+s[38])/1000
                    max_z = ((s[39]*65536)+(s[40]*256)+s[41])/1000
                    min_x = ((s[42]*65536)+(s[43]*256)+s[44])/1000
                    min_y = ((s[45]*65536)+(s[46]*256)+s[47])/1000
                    min_z = ((s[48]*65536)+(s[49]*256)+s[50])/1000
                    ctemp = ((s[51]*256)+s[52])
                    battery = ((s[18]*256)+s[19])
                    voltage = 0.00322*battery
                    '''
                    return rms_x,rms_y,rms_z

# Creating the Animation object
ani = animation.FuncAnimation(fig, update_lines, frames=200, interval=5, blit=False)
plt.show()
