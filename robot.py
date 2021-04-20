import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time


class ROBOT:
    def __init__(self, solutionID, swarmID):
        self.motors = {}

        self.robot = p.loadURDF("body" + str(swarmID) + ".urdf")
        pyrosim.Prepare_To_Simulate("body" + str(swarmID) + ".urdf")
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.PrepareToSense()
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        self.myID = solutionID


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

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self, swarmID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        outFile = open("tmp"+str(self.myID) + "." + str(swarmID) + ".txt", "w")
        outFile.write(str(xPosition))
        outFile.close()
        os.system("rename tmp"+str(self.myID)+ "." + str(swarmID) + ".txt fitness"+str(self.myID)+ "." + str(swarmID) +".txt")
