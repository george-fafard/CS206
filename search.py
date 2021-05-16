import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c


# A/B testing code
mode = ""

for q in range(0, 2):
    if q == 0:
        mode = 'A'
        print(mode)
    else:
        mode = 'B'
        print(mode)
    for i in range(0, c.A_B_TESTS):
        phc = PARALLEL_HILL_CLIMBER(mode, i)
        phc.Evolve()
        # phc.Show_Best()
        phc.Write_Data()

# # for demonstration
# phc = PARALLEL_HILL_CLIMBER("A", 0)
# phc.Evolve()
# phc.Show_Best()
