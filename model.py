#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 22:45:32 2020

@author: toriliang
"""


import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import numpy
import matplotlib.animation 


def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

#environment.append(rowlist)
#rowlist.append(value)
rowlist = []
environment = []
#distance = [] 
#f=open("in.txt",delimiter=',')
#data = csv.reader(f)

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#frames, = ax.plot(x, y)

with open("in.txt") as f:
    data = f.read().splitlines() 

    for row in data:
        rowlist = []
        for value in row.split(','):
            if value[-1] == '\\':
                value1 = value[0:(len(value)-1)]
                rowlist.append(int(value1))
            else:
                rowlist.append(int(value))
        environment.append(rowlist)

for line in agents:
    f.write(line)
#f.close()


# Make the agents.
for i in range(num_of_agents):
    
    agents.append(agentframework.Agent(environment, agents, neighbourhood))
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

carry_on = True

def update(frame_number):
    fig.clear()   
    global carry_on
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move("frame_number")
            agents[i].eat()
            agents[i].share_with_neighbours()
            
    for self in agents:
        for agent in agents:
            distance = distance_between(self, agent)    
    
    #print("distance: %s" % distance)
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.title(label = "Scatter Plot Animation")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #matplotlib.pyplot.draw()
        matplotlib.pyplot.show()
        
     
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update,frames=gen_function, repeat=False)

    
matplotlib.pyplot.show()










