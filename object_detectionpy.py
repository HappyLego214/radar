import math
import matplotlib.pyplot as plt

radar_range = 100
radar_position = (0,0)

objects_in_area = [(50,30), (5,10), (120,50), (10,500)]
sectors = {'top-left': [(-100, 0), (0,100)], 
           'top-right': [(0, 100), (100, 0)],
           'bottom-left': [(-100, 0), (0, -100)],
           'bottom-right': [(0, -100), (100, 0)]
           }

def calcDistance(radar, object):
    distance = math.sqrt(math.pow((radar[0] - object[0]), 2) + math.pow((radar[1] - object[1]), 2))
    return distance

detected_objects = []
for object in objects_in_area:
    distance = calcDistance(radar_position, object)
    if distance <= radar_range:
        detected_objects.append(object)
        
print(f"Number of Detected Objects: {len(detected_objects)} | Detected Objects: {detected_objects}")
        
plt.figure()
plt.scatter(*radar_position, color='red', label='radar')
plt.scatter(*zip(detected_objects), color='green', label='detected objects')
plt.xlim(-radar_range, radar_range)
plt.ylim(-radar_range, radar_range)
plt.legend()
plt.show()