# Import the random module using the import statement.
import random 

# Build the Agent class.
class Agent:
    
    # Define the initialization method.
    def __init__(self, environment, agents, neighbourhood): # 3 formal parameters.
        self.environment = environment     # Pass the environment list to the Agent's constructor.
        self.store = 0
        self.y = random.randint(0,99)      # Generate a random number between 0 and 99 and assign it to y.
        self.x = random.randint(0,99)      # Generate a random number between 0 and 99 and assign it to x.
        self.agents = agents     # Assigns externally passed parameter values to its own variables within the Agent class.
        self.neighbourhood = neighbourhood # Pass a value to instance.neighbourhood from externally parameter.
        
    # Define the move method, use if...else statement and Torus to deal with boundary issues.
    def move(self, frame_number):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
    
    # Define the eat method, use if statement to work out.
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
        self.store += 10   
        
    # Creat this method to calculate the distance to each of the other agents.
    def share_with_neighbours(self):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= self.neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))
                
    # Define distance_between method to calculate distance.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
   

# Creat objects to test.
#a = Agent("environment","agents","neighbourhood")
#print(a)
#a.move("frame_number")
#print(a.y, a.x)






