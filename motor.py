import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.LOOPS)

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,  # in radians

            targetPosition=desiredAngle,  # in radians

            maxForce=c.newtons)  # in newton meters

    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "out.npy", self.motorValues)
