import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import numpy
import matplotlib.animation # import animation from matplotlib package.

num_of_agents = 10      # Make a num_of_agents variable and assign it to 10
num_of_iterations = 100 # Make a num_of_iterations variable and assign it to 100
neighbourhood = 20      # Make a neighbourhood variable and assign it to 20
agents = []             # Creat agents list.
environment = []        # Creat environment list.

# Make animation properties.
fig = matplotlib.pyplot.figure(figsize=(6, 6)) # Set up the figure and the plot size.
ax = fig.add_axes([0, 0, 1, 1])  # Add axis list in the figure.

#frames, = ax.plot(x, y)

# To load in.txt file.
with open("in.txt") as f:
    data = f.read().splitlines() 
# The downloaded text format is not standard, so needs to change.
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


# # Make the agents by putting into a for-loop.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)  # Make scatter plot.
    
#matplotlib.pyplot.show()

# Start condition.
carry_on = True  

# Update data points.
def update(frame_number): # Sets the number of animation frames
    fig.clear()     # Clear a figure.
    global carry_on # carry_on is a global variable
    
    # Move the agents by putting into nest for-loops.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move("frame_number")
            agents[i].eat()
            agents[i].share_with_neighbours()
    
    """
    # Set stopping condition.
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    """
    
    # Set properties and show the animation plot.
    matplotlib.pyplot.xlim(0, 100)         # Set the x-axis range from 0 to 100.
    matplotlib.pyplot.ylim(0, 100)         # Set the y-axis range from 0 to 100.
    matplotlib.pyplot.imshow(environment)  # Display an image on the axes.
    matplotlib.pyplot.title(label = "Scatter Plot Animation") # Set plot title.
    
    # Displays the random points obtained with the for-loop.
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.show()        
 
# Define a generator function.
def gen_function(b = [0]):
    a = 0
    global carry_on # Display clearly, even if it is not assigned.
    while (a < num_of_agents) & (carry_on) :  # While-loop.
        yield a			# Returns control and waits next call.
        a = a + 1

# Use for-each loop iterator to put out agents.        
for self in agents:
    for agent in agents:
        agentframework.Agent.distance_between(self, agent) # Calling the method from agentframework.py.

# Make the animation stopping condition.
animation = matplotlib.animation.FuncAnimation(fig, update,frames=gen_function, repeat=False)

# Show the plot animation.    
matplotlib.pyplot.show()

# Save .gif file.
#animation.save('test_animation.gif',writer='imagemagick')




