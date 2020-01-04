import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import numpy
import matplotlib.animation 

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
#rowlist = []
environment = []

# Make animation properties.
fig = matplotlib.pyplot.figure(figsize=(6, 6))
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
    
#matplotlib.pyplot.show()

carry_on = True

# Update data points.
def update(frame_number):
    fig.clear()   
    global carry_on
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move("frame_number")
            agents[i].eat()
            agents[i].share_with_neighbours()
            
    # Set stopping Animation condition.
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.title(label = "Scatter Plot Animation")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.show()        
     
def gen_function(b = [0]):
    a = 0
    global carry_on # Display clearly, even if it is not assigned.
    while (a < num_of_agents) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

for self in agents:
    for agent in agents:
        agentframework.Agent.distance_between(self, agent) 

# Make the animation.
animation = matplotlib.animation.FuncAnimation(fig, update,frames=gen_function, repeat=False)

# Show the plot animation.    
matplotlib.pyplot.show()





