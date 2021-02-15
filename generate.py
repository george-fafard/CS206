import pyrosim.pyrosim as pyrosim


# this is the data pyrosim will generate
pyrosim.Start_SDF("boxes.sdf")  # name of our world

x = 0
y = 0
z = 0.5
num_columns = 0

while num_columns < 6:
    if num_columns > 0:
        x += 1
    num_rows = 0
    y = 0
    while num_rows < 6:
        if num_rows > 0:
            y += 1
        length = 1
        width = 1
        height = 1
        num_box = 0
        while num_box < 10:
            if num_box > 0:
                height = height * 0.9
                width = width * 0.9
                length = length * 0.9
                pyrosim.Send_Cube(name="Box"+str(num_columns + num_rows + num_box + 1), pos=[x, y, z + num_box*0.9], size=[length, width, height])  # make a box :D
            else:
                pyrosim.Send_Cube(name="Box", pos=[x, y, z],
                                  size=[length, width, height])  # make a box :D
            num_box += 1
        num_rows += 1
    num_columns += 1
pyrosim.End()  # the end
