import pybullet as p
import time as t
import pybullet_data


LOOPS = 1000
current_loop = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
while current_loop < LOOPS:

    p.stepSimulation()
    t.sleep(0.00166)
    current_loop += 1
    print(current_loop)



p.disconnect()