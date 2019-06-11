# Random-molecule-in-space-generator-
The program for random trajectory simulation of the set number of particles.

TASK: 
Simulate   a   random   movement   of   particles   within   30x30x30   cubic  
3D   space.   This   particles   are   to   connect   into   dimers (pairs)   when   they   encounter  
each   other.   There   is   a   50%   probability   for   the   dimers   to   detach.   Boundary  
conditions are to be applied. 
 
Each   particle   is   a   separate   instance   of   the   particle   class,   with   its  
intrinsic   defined   characteristics.   This   characteristics,   among   the   others  
include   the   definition   of   a   movement   of   single   particle,   as   well   as  
movement of particles that are in a dimer.

particle.py contains a definition of a class particle, and describes the behaviour of each particle, contraints of movement etc.
simulation.py is the main program, describes the simulation details and writes it into the output file containing coordinates in space of eacg particle over the time in the form of vectors (x, y, z). The output file is written in a from of .xyz file and is an input for the visualization programs such as VMD.
