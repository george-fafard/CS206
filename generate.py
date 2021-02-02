import pyrosim.pyrosim as pyrosim


# this is the data pyrosim will generate
pyrosim.Start_SDF("box.sdf")  # name of our world
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])  # make a box :D

pyrosim.End()  # the end
