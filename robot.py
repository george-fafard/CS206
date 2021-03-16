import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.motors = {}

        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.PrepareToSense()
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def PrepareToSense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, index):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(index)

    def Act(self, index):
        # for motor in self.motors:
        #     self.motors[motor].Set_Value(self.robot, index)
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
                print(neuronName, jointName, desiredAngle)



    def Think(self):
        self.nn.Update()