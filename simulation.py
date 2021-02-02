import pybullet as p
import time as t


LOOPS = 1000
current_loop = 0

physicsClient = p.connect(p.GUI)
while current_loop < LOOPS:

    p.stepSimulation()
    t.sleep(0.00166)
    current_loop += 1
    print(current_loop)



p.disconnect()