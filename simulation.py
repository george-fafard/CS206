from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import pybullet_data
import time as t
import os


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI.lower() == "direct":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.GRAV_X, c.GRAV_Y, c.GRAV_Z)
        self.world = WORLD()
        self.robots = []
        for i in range(0, c.swarmSize):
            self.robots.append(ROBOT(solutionID, i))

    def Run(self, directOrGUI):
        for i in range(0, c.LOOPS):
            p.stepSimulation()
            for bot in self.robots:
                bot.Sense(i)
                bot.Think()
                bot.Act(i)
            # motors!!
            # back leg
            # front leg
            if directOrGUI.lower() == "gui":
                t.sleep(c.fraction_second)

    def __del__(self):
        # for sensor in self.robot.sensors:
        #     self.robot.sensors[sensor].Save_Values()
        # for motor in self.robot.motors:
        #     self.robot.motors[motor].Save_Values()
        os.system("del brain*.nndf")
        os.system("del body*.urdf")
        p.disconnect()

    def Get_Fitness(self):
        for i in range(0, c.swarmSize):
            self.robots[i].Get_Fitness(i)