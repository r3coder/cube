# CUBE
CUBE is a esoteric programming language (esolang) that uses rubik's cube's structure as data structure. CUBE is Turing complete since it uses hypercubes.

# Basic explaination
Imagine a 3x3x3 Rubik's CUBE. Also, imagine there's number on every square that you look. If you twist the cube, then you can move numbers to other plane. This is how CUBE handles most of operations.

## Cube twisting
You can twist cube to move value

<img src="https://github.com/r3coder/cube/blob/master/img/img_rotation.png" width="400">

ex) ``LR'FFBBLR'DD```: Move value from plane 2 to plane 5

## Data structure
Each CUBE has total of 55 (6x9+1) data spaces.
 - ***Data Cell***(6 x 8-bit): Data cells are cell that is placed on center of each plane. Each cell can hold 8-bit data, and each cell is unique. Number in parenthesis indicates location of each cell if it is placed on normal d6.
   - ***Input Cell***(2): Any Input number is loaded on this cell.
   - ***Output Cell***(5): If user executes print, then print ascii from this cell.
   - ***Static 1 Cell***(1): This only cell is always fixed to 1. You can't change the value of this cell with any kind of operations.
   - ***NOT Cell***(6): Operates at when **Execute** Command executed. Computes bit-wise NOT between saved data in itself and Bit cells, and place result at itself.
   - ***OR Cell***(3): Operates at when **Execute** Command executed. Computes bit-wise OR between saved data in itself and Bit cells, and place result at itself.
   - ***AND Cell***(4): Operates at when **Execute** Command executed. Computes bit-wise AND between saved data in itself and Bit cells, and place result at itself.
 - ***Bit Cell***(48 x 1-bit): Around the each data cell, there is 8 bit cells on each plane. These cells are movable with twisting the cube.
 - ***Core Cell***(1 x 32-bit): The Core cell is one very special cell that isn't visible outside. It can hold 32-bit data, and you can only add or subtract to this cell using Input cell. More explanation is described down below.

## Core Cell
This cell acts as 32-bit register, that can only check if it is zero using ```(``` and ```)```. You can put values from Input using ```!```(and +1 / -1 for ```+``` and ```-```). You can't pull out value from this cell.
 
# Hypercube
Hypercube is very special concept that make CUBE is complete turing machine. We suppose that there is CUBE inside CUBE, and CUBE outside CUBE for 4-th dimension direction.
You can shift using ```[``` and ```]```, then you can move to inner cube or outer cube.
Also, you can use ```{``` and ```}``` to send Data Cell's value to inner cube or outer cube.
Still, we can only access 1 CUBE each time, so you have to move to other CUBE if you want to execute other CUBE's command.


# Commands List

## Cube twisting
Basically, it is same as basic cube rotating characters
 - ```U / U' / D / D' / L / L' / R / R' / B / B' / F / F'```: Turn a CUBE at corresponding direction.
 - ```u / u' / d / d' / l / l' / r / r' / b / b' / f / f' / M / M' / S / S' / E / E'```: Turn a CUBE at corresponding direction, still CUBE's center is fixed, so these are somewhat depreciated on this compiler.
 
## I/O and Operations
 - ```I```: Input value and put to the Input cell.
 - ```P```: Print from the Output Cell as ascii.
 - ```*```: Load Data cells to Bit cells.
 - ```=```: Save Bit cells' data to Data cells, but Static Cell remains to 1.
 - ```X```: Execute commands(AND, OR, NOT) in each planes and store result in Data cells.
 - ```C```: Clear all Data cells' data to 0, but Static Cell remains to 1.
 
## Core Cells
 - ```(```: If the Core cell's value is same as 0, find matching ```)``` and execute next character of matching ```)```. Else, execute next character.
 - ```)```: If the Core cell's value is same as 0, execute next charater, else, find matching```(```and execute next character.
 
 - ```!```: Set Input cell's value to the Core cell.
 - ```+```: Add Input cell's value to the Core cell.
 - ```-```: Subtract Input cell's value to the Core cell.
 - ```m```: Subtract Static 1 cell's value(Actually 1) of the Core cell. (Possibility to Removed)
 - ```p```: Add Static 1 cell's value(Actually 1) of the Core cell. (Possibility to Removed)

## HyperCube
 - ```{```: Send All 6 Data Cells' data to inner cube's Data Cells.
 - ```}```: Send All 6 Data Cells' data to outer cube's Data Cells.
 - ```[```: Move to inner cube.
 - ```]```: Move to outer cube.

## Extend Input
Extended input is allowed on some operations to make programming easier. (Maybe) These operations are not necessary
ex) ```3=```: Load only plane 3
 - ```0```: Select all planes
 - ```1```, ```2```, ```3```, ```4```, ```5```, ```6```: Select specific plane
Available Commands With extended input
   - ```*```
   - ```=```
   - ```X```: Only 3,4,5 plane
   - ```C```

# Files and usage
 - cube.py: CUBE and CUBES Class implementation
 - cube_compiler.py: CUBE Compiler
 - command_finder.py: Find shortest command to make specific plane has specific value
 - examples/: Examples
   - hello_world.cube: Print ("Hello, world!")
   - basic_if.cube: Basic if statement
 - README.md: This file
