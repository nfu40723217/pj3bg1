# pip install pyzmq cbor keyboard
from zmqRemoteApi import RemoteAPIClient
import keyboard

client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')

# Define the size and position of the cuboid
size = [0.1, 0.2, 0.3]
position = [0, 0, 0.15]

# Create the cuboid
#cuboid = sim.createPureShape(0, 8, size, 1, None)
#sim.setObjectPosition(cuboid, -1, position)

sim.startSimulation()
print('Simulation started')

def setBubbleRobVelocity(leftWheelVelocity, rightWheelVelocity):
    leftMotor = sim.getObject('/leftMotor')
    rightMotor = sim.getObject('/rightMotor')
    sim.setJointTargetVelocity(leftMotor, leftWheelVelocity)
    sim.setJointTargetVelocity(rightMotor, rightWheelVelocity)

'''
# Example usage 1:
setBubbleRobVelocity(1.0, 1.0)
time.sleep(2)
setBubbleRobVelocity(0.0, 0.0)
'''
# use keyborad to move BubbleRob

while True:
    if keyboard.is_pressed('up'):
        setBubbleRobVelocity(5.0, 5.0)
    elif keyboard.is_pressed('down'):
        setBubbleRobVelocity(-3.0, -3.0)
    elif keyboard.is_pressed('left'):
        setBubbleRobVelocity(-2.0, 2.0)
    elif keyboard.is_pressed('right'):
        setBubbleRobVelocity(2.0, -2.0)
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setBubbleRobVelocity(0.0, 0.0)




