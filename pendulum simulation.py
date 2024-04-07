# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:11:05 2024

@author: Nikita Rana
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio

def makeGif(x,y,name):
    !mkdir frames
    
    counter=0
    images = []
    for i in range(0,len(x)):
        plt.figure(figsize = (6,6))

        plt.plot([0,x[i]],[0,y[i]], "o-", color = "b", markersize = 7, linewidth=.7 )
        plt.title("Pendulum")
        plt.xlim(-1.1,1.1)
        plt.ylim(-1.1,1.1)
        plt.savefig("frames/" + str(counter)+ ".png")
        images.append(imageio.imread("frames/" + str(counter)+ ".png"))
        counter += 1
        plt.close()

    imageio.mimsave(name, images)

    !rm -r frames

def simple_pendulum(theta_0, omega, t, phi):
    theta = theta_0*np.cos(omega*t + phi)
    return theta

#parameters of our system
theta_0 = np.radians(15) #degrees to radians

g = 9.8 #m/s^2
l = 1.0 #m
omega = np.sqrt(g/l)

phi = 0 #for small angle

time_span = np.linspace(0,20,300) #simulate for 20s split into 300 time intervals
theta = []
for t in time_span:
    theta.append(simple_pendulum(theta_0, omega, t, phi))

x = l*np.sin(theta)
y = -l*np.cos(theta) 
#negative to make sure the pendulum is facing down pendulum
def full_pendulum(g,l,theta,theta_velocity, time_step):
    theta_acceleration = -(g/l)*np.sin(theta)
    theta_velocity += time_step*theta_acceleration
    theta += time_step*theta_velocity
    return theta, theta_velocity

g = 9.8 #m/s^2
l = 1.0 #m

theta = [np.radians(90)] #theta_0
theta_velocity = 0
time_step = 20/300

time_span = np.linspace(0,20,300) #simulate for 20s split into 300 time intervals
for t in time_span:
    theta_new, theta_velocity = full_pendulum(g,l,theta[-1], theta_velocity, time_step)
    theta.append(theta_new)

#Convert back to cartesian coordinates 
x = l*np.sin(theta)
y = -l*np.cos(theta)

#Use same function from simple pendulum
makeGif(x,y,"pendulum.gif")