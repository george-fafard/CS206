import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import matplotlib as plt
import numpy as np


LOOPS = 1000
current_loop = 0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = np.zeros(LOOPS)
frontLegSensorValues = np.zeros(LOOPS)
for i in range(0,  LOOPS):

    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    t.sleep(0.00166)

np.save("data/backlegout.npy", backLegSensorValues)
np.save("data/frontlegout.npy", frontLegSensorValues)

p.disconnect()