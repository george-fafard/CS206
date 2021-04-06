import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time


class SOLUTION:
    def __init__(self, ID):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.myID = ID

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomCol = random.randint(0, 1)
        self.weights[randomRow, randomCol] = random.random() * 2 - 1

    def Start_Simulation(self, dOrG):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        # go go go
        os.system("start /B python simulate.py " + dOrG + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)

        inFile = open("fitness"+str(self.myID)+".txt", 'r')
        self.fitness = float(inFile.read())
        inFile.close()
        os.system("del fitness"+str(self.myID)+".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")  # name of our world
        pyrosim.Send_Cube(name="Box", pos=[c.x + 1.5, c.y + 1.5, c.z], size=[c.length, c.width, c.height])  # make a box :D
        pyrosim.End()  # the end

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[c.x, c.y, c.z + 1], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0.5 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[c.x + 0.5, c.y, c.z - 1], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="-0.5 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[c.x - 0.5, c.y, c.z - 1], size=[c.length, c.width, c.height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID
