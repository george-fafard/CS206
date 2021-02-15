import pyrosim.pyrosim as pyrosim


# this is the data pyrosim will generate


x = 0
y = 0
z = 0.5
length = 1
width = 1
height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")  # name of our world
    pyrosim.Send_Cube(name="Box", pos=[x + 1.5, y + 1.5, z], size=[length, width, height])  # make a box :D
    pyrosim.End()  # the end


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z+1], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_Front_Leg", parent="Torso", child="FrontLeg", type="revolute", position="0.5 0 1")
    pyrosim.Send_Cube(name="FrontLeg", pos=[x+0.5, y, z-1*], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_Back_Leg", parent="Torso", child="BackLeg", type="revolute", position="-0.5 0 1")
    pyrosim.Send_Cube(name="BackLeg", pos=[x-0.5, y, z-1], size=[length, width, height])
    pyrosim.End()


Create_Robot()
Create_World()
