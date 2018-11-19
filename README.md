# Numerics_Assignment_CAW_restart
The Report_Generator.py file, calls the other files to create a range of graphs and tables, all of which are stored in the "figures" folder. Please note that only the final graph is displayed. The file takes approx 2:40 min to run.
All_schemes.py contains five advection schemes: FTBS, CTCS, LW, WB, Combi.
Initial_conditions.py contains four sets of initial conditions.
frame.py generates graphs and tables for the first three schemes for all initial conditions as well as boundedness graphs.
Error_checks.py contains RMS error and Linf error calculations.
Order.py contains code to check for errors across different dx lengths and calculates convergence rates.
Time_time_steps.py calculates computation time for first three schemes.
Conclusion.py completes the same tasks as frame.py, but for the last three schemes together.
Conclusion_Time_time_steps.py calculates computation time for last three schemes.
