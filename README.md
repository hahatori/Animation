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

### The core parameters of the **animation** are ```frames``` and ```func```.

**Frames** are the range of frames in the animation and are essentially a data generator.

**Func** is a callback function that is called every time it is updated, so we just need to update the number in the figure in this function.

In fact, **frames** determine the range of values for the entire animated frame, iterating once in the interval and then passing the value to **func** until the entire frames iteration is complete.

## Theoretical Results

The model refers to methods such as ```eat``` ，```move``` and ```share_with_neighbours``` from the **agentframework.py**, which are shown on the animation.

## Actual Results

![Animation](https://github.com/hahatori/Python_Assignment1/blob/master/Ani.mov)

## Issues

1. Using ```anim.save('test_animation.gif',writer='imagemagick')``` to save **test_animation.gif** file.

2. When you want to stop the animation, use the following statement ```animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)```


