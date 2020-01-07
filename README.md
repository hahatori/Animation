# Animation

Use animation functions of matplotlib package, get it animated.

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

### Animation

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

### The core parameters of the **animation** are ```frames``` and ```func```.

**Frames** are the range of frames in the animation and are essentially a data generator.

**Func** is a callback function that is called every time it is updated, so we just need to update the number in the figure in this function.

In fact, **frames** determine the range of values for the entire animated frame, iterating once in the interval and then passing the value to **func** until the entire frames iteration is complete.

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

 

## Actual Results

![Animation](https://github.com/hahatori/Python_Assignment1/blob/master/Ani.mov)

## Issues

1. 
2. 
3. 

