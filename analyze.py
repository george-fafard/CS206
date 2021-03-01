import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load("data/backlegout.npy")
frontLegSensorValues = np.load("data/frontlegout.npy")
targetAngles = np.load("data/sinout.npy")


plt.plot(backLegSensorValues, label="Back Leg", linewidth=3)
plt.plot(frontLegSensorValues, label="Front Leg")
plt.plot(targetAngles, label="sine")
plt.legend()

plt.show()
