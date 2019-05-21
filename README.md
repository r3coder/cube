# CUBE
CUBE is a esoteric programming language (esolang) that uses rubik's cube's structure as data structure. CUBE is Turing complete since it uses hypercubes.

# Files
 - main.py : CUBE Compiler
   - Basic commands are working
   - *IF* and *HYPERCUBE* is not implemented yet...

# Basic explaination
CUBE

# Data structure
Each CUBE has total of 54 (6x9) spaces. For each side, there are one center cell that can hold 8-bit data. We call this ***Center Cell*** or ***Center*** And around the center cell, there are 8 cells that only hold 1-bit data. We call this ***Around Cell*** or ***Around***.

 - 1: Static 1
 - 2: Input
 - 5: Output
 - 3: OR
 - 4: AND
 - 6: NOT

# Hypercube
Hypercube is very special concept. For CUBE to be a complete turing machine, we suppose that there is cube inside cube, and cube outside cube in a 4-th dimension.

Still, we can only access 1 cube each time, so you have to move to other cube if you want to execute other cube's command.


# Basic Commands

## Cube spining
Basically, it is same as basic cube rotating characters
 - ```U / U' / D / D' / L / L' / R / R' / B / B' / F / F'```: Turn cube at corresponding direction.
 - ```u / u' / d / d' / l / l' / r / r' / b / b' / f / f' / M / M' / S / S' / E / E'```: Turn cube at corresponding direction, still cube's center is fixed (for this only compiler).
 
 
## I/O and Operations
 - ```I```: Get a character and put that number into input cell(top)
 - ```P```: Print a number in ascii
 - ```*```: Load center cell to around cell.
 - ```=```: Save around cell's data to center cell.
 - ```X```: Execute commands(AND, OR, NOT) in each planes and store result in center cell.
 - ```C```: Clear all center cell's data to 0, except for static 1.
 
## IF
 - ```?(```: If corresponding cell's value is same as 0, find matching ```)``` and execute next character of matching ```)```. Else, execute next character.
   - ? index: 0 for all cells, 1~6 for each cells. (Will be explained more later)
 - ```)```: If corresponding cell's value is same as 0, execute next charater, else, find matching```(```and execute next character.
    ex) 4(ULDDL'U')

## HyperCube
 - ```[```: Send 6 Center data to inner cube.
 - ```]```: Send 6 Center data to outer cube.
 - ```{```: Move to inner cube.
 - ```}```: Move to outer cube.
