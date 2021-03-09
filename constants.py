import numpy as np

# common constants
LOOPS = 1000
fraction_second = 1/240
GRAV_X = 0
GRAV_Y = 0
GRAV_Z = -9.8

# front leg values
amplitude_front = np.pi/6.0
frequency_front = 6
phaseOffset_front = np.pi/4.0

# back leg values
amplitude_back = np.pi/2.0
frequency_back = 6
phaseOffset_back = 0

newtons = 8  # Force for motors

# target stuff calculated from leg values

targetAngles_front = amplitude_front * np.sin(frequency_front * np.linspace(-np.pi, np.pi, LOOPS) + phaseOffset_front)