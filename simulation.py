from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import pybullet_data
import time as t


class SIMULATION:
    def __init__(self, directOrGUI):
        if directOrGUI.lower() == "direct":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.GRAV_X, c.GRAV_Y, c.GRAV_Z)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self, directOrGUI):
        for i in range(0, c.LOOPS):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
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
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()