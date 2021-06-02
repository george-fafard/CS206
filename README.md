# CS206 Evolutionary Robotics Final project
This branch contains the final iteration of the term long project for Evolutionary Robotics. My project simulates a swarm of robots acting with a single neural network brain that attempts to randomly change motor values and evolve over generations. 

# Viewing Result Data
The result .npy files can be ran using the "plotFitnessValues.py" file. This will use matplotlib pyplot to display some graphs.

# Running the Simulation
Running With New Data Writing:
The simulation can be ran by running the "search.py" file. Before running search, values can be changed in "constants.py" to run less generations and such.

Running Without Writing New Data:
Comment out the part of "search.py" that has the for loop and the if else. Uncomment the commented code at the bottom labelled for demonstration.
