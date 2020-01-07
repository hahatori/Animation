# Animation

Make agents talking to each other by altering each other's variables

This project including [in.txt](https://github.com/hahatori/Animation/blob/master/in.txt), [agentframework.py](https://github.com/hahatori/Animation/blob/master/agentframework.py) and [model.py](https://github.com/hahatori/Animation/blob/master/model.py).

## Contents

- [Details](#details)
- [Theoretical Results](#theoretical-results)
- [Actual Results](#actual-results)
- [Issues](#issues)

## Details

### The key elements:

**in.txt** is a text file with raster data.

**Agent** code can build agents to interact.

**Model** code can creat models for connecting developers and users.

### The self 

**self** represents an instance of a class, not a class. ```self.class ``` points to the class.

```sh
$ class Agent:       
      def eat(self): 
          print(self)
          print(self.__class__)
      
  a = Agent() 
  print(a)
  a.eat()  
```
Output:

```sh
$ <__main__.Agent object at 0x12253fc10>
  <__main__.Agent object at 0x12253fc10>
  <class '__main__.Agent'>
```

**self** needs to be defined at definition time, but is passed in automatically when called :

```sh
$ class Agent(object): 
  def __init__(self, name, age): 
    self.name = name 
    self.age = age 
  
  def SetName(self,name): 
    self.name = name 
  
  def SetAge(self,age): 
    self.age = age 
  
  def GetName(self): 
    return self.name 
  
  def GetAge(self): 
    return self.age 
  
u = User('Obama',17) 
print u.GetName() 
print u.GetAge() 
```

Output:

```sh
$ Obama
  17
```

## Theoretical Results

**Communication** allows programs to run to adjust each other's variables, or to call functions within each other and pass information, or to retrieve information from each other.

Move below statement to **agentframework.py** :

```sh
$ def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
```

Then use ```agentframework.Agent.distance_between(self, agent)``` to call it in the model. 

## Actual Results

![Plot](https://github.com/hahatori/Python_Assignment1/blob/master/Communi.png)

## Issues

1. The reason you can access data everywhere in the class is that you're essentially binding this thing called **self**. It's the first argument to the method. Instead of calling **self**, you can call it something else, self is just a convention.

2. When you creat the **share_with_neighbours** method, this method calculates the distance between the agents and the its neighbor by iterating through the parameter values passed in from the outside. If distance is less than or equal to the neighbourhood, divide sum by two to calculate average then pass the average values on to self.store and agent.store.

3. How does the model import and execute the commands in agents.


