# CUBE
CUBE is a esoteric programming language (esolang) that uses rubik's cube's structure as data structure. CUBE is Turing complete since it uses hypercubes.

# Files
 - main.py : CUBE Compiler
   - Basic commands are working
   - *IF* and *HYPERCUBE* is not implemented yet...

# Basic explaination
Imagine a 3x3x3 Rubik's CUBE. is basic unit 

## 

## Data structure
Each CUBE has total of 55 (6x9+1) data spaces.
 - ***Data Cell***(6 x 8-bit): Data cells are cell that is placed on center of each plane. Each cell can hold 8-bit data, and each cell is unique. Number in parenthesis indicates location of each cell if it is placed on normal d6.
   - ***Input Cell***(2): 
   - ***Output Cell***(5): 
   - ***Static 1 Cell***(1): This only cell is always fixed to 1. You can't change the value of this cell with any kind of operations.
   - ***NOT Cell***(6): Operates at when **Execute** Command executed. Computes bit-wise NOT between saved data in itself and Bit cells, and place result at itself.
   - ***OR Cell***(3): Operates at when **Execute** Command executed. Computes bit-wise OR between saved data in itself and Bit cells, and place result at itself.
   - ***AND Cell***(4): Operates at when **Execute** Command executed. Computes bit-wise AND between saved data in itself and Bit cells, and place result at itself.
 - ***Bit Cell***(48 x 1-bit): Around the each data cell, there is 8 bit cells on each plane. These cells are movable with twisting the cube.
 - ***Core Cell***(1 x 32-bit): The Core cell is one very special cell that isn't visible outside. It can hold 32-bit data, and you can only add or subtract to this cell using Input cell. Also, you can 
 
# Hypercube
Hypercube is very special concept. For CUBE to be a complete turing machine, we suppose that there is cube inside cube, and cube outside cube in a 4-th dimension.

Still, we can only access 1 cube each time, so you have to move to other cube if you want to execute other cube's command.


# Basic Commands

## Cube spining
Basically, it is same as basic cube rotating characters
 - ```U / U' / D / D' / L / L' / R / R' / B / B' / F / F'```: Turn cube at corresponding direction.
 - ```u / u' / d / d' / l / l' / r / r' / b / b' / f / f' / M / M' / S / S' / E / E'```: Turn cube at corresponding direction, still cube's center is fixed (for this only compiler).
 
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
 
 - ```!```: Put Input cell's value to the Core cell.
 - ```-```: Subtract Static 1 cell's value(Actually 1) of the Core cell. (Possibility to Removed)
 - ```+```: Add Static 1 cell's value(Actually 1) of the Core cell. (Possibility to Removed)

## HyperCube
 - ```[```: Send All 6 Data Cells' data to inner cube's Data Cells.
 - ```]```: Send All 6 Data Cells' data to outer cube's Data Cells.
 - ```{```: Move to inner cube.
 - ```}```: Move to outer cube.
