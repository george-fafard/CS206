import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r


LOOPS = 1000
fraction_second = 1/240
current_loop = 0


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = np.zeros(LOOPS)
frontLegSensorValues = np.zeros(LOOPS)

amplitude_back = np.pi/2.0
frequency_back = 6
phaseOffset_back = 0
targetAngles_back = amplitude_back * np.sin(frequency_back * np.linspace(-np.pi, np.pi, LOOPS) + phaseOffset_back)

amplitude_front = np.pi/6.0
frequency_front = 6
phaseOffset_front = np.pi/4.0
targetAngles_front = amplitude_front * np.sin(frequency_front * np.linspace(-np.pi, np.pi, LOOPS) + phaseOffset_front)


for i in range(0,  LOOPS):

    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # motors!!
    # back leg
    newtons = 8
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_Back_Leg",

        controlMode=p.POSITION_CONTROL,  # in radians

        targetPosition=targetAngles_back[i],  # in radians

        maxForce=newtons)  # in newton meters

    # front leg
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_Front_Leg",

        controlMode=p.POSITION_CONTROL,  # in radians

        targetPosition=targetAngles_front[i],  # in radians

        maxForce=newtons)  # in newton meters

    t.sleep(fraction_second)

np.save("data/backlegout.npy", backLegSensorValues)
np.save("data/frontlegout.npy", frontLegSensorValues)


p.disconnect()