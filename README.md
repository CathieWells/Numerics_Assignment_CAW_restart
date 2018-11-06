# Numerics_Assignment_CAW_restart
All files for new version of numerics modelling
The initial conditions, error checks and advection scheme methods (FTBS, CTCS and LW) are all called from the frame functions.  
Frames involving just one scheme allow a choice of initial conditions based on 1) Cos bell curve, 2) Square wave, 3) Mixed wave.
Frames involving just one set of initial conditions plot all three schemes along with initial conditions onto one graph.
All frame calls allow number of time steps and number of spatial steps to be defined as parameters of the function.
Frame calls of single schemes also need parameter for condition to be set.
Graphs are saved with their specific parameters in the title to prevent over writing.
Frames of all 3 schemes generate error tables for comparison which are saved with reference to resolution and initial conditions.
