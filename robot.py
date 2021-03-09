import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c


class ROBOT:
    def __init__(self):

        self.motors = []
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.PrepareToSense()
        self.PrepareToAct()

    def PrepareToSense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def PrepareToAct(self):
        self.motors = {}
        self.amplitude = c.amplitude_back
        self.frequency = c.frequency_back
        self.phaseOffset = c.phaseOffset_back
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            self.motors[jointName].motorValues = self.amplitude * np.sin(self.frequency * np.linspace(-np.pi, np.pi, c.LOOPS) + self.phaseOffset)

    def Sense(self, index):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(index)

    def Act(self, index):
        for motor in self.motors:
            self.motors[motor].Set_Value(self.robot, index)
