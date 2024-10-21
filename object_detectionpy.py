import math
import matplotlib.pyplot as plt

radar = {'position': (0,0), 'range': 100}

objects_in_area = [(-50,10), (50,30), (80,-50), (-10,-80)]
sector_bounderies = {
    'top-left': [(-100, 0), (0,100)], 
    'bottom-left': [(-100, 0), (0, -100)],
    'top-right': [(0, 100), (100, 0)],
    'bottom-right': [(0, -100), (100, 0)],
    }        

def calcDistance(radar, object):
    distance = math.sqrt(math.pow((radar[0] - object[0]), 2) + math.pow((radar[1] - object[1]), 2))
    return distance

def scanQuadrant(sector, object):
    x1, y1 = sector[0]
    x2, y2 = sector[1]
    if min(x1, x2) <= object[0] <= max(x1, x2) and min(y1, y2) <= object[1] <= max(y1, y2):
        return True
    return False

def scanRadar(sectors, objects_in_area, radar):
    sector_objects = {
    'top-left': [], 
    'bottom-left': [],
    'top-right': [],
    'bottom-right': [],
    }
    
    for idx, sector in sectors.items():
        for obj in objects_in_area: 
            obj_in_quad = scanQuadrant(sector, obj)
            if obj_in_quad == True:    
                distance = calcDistance(radar['position'], obj)
                if distance <= radar['range']:
                    sector_objects[idx].append(obj)
            continue
    
    return sector_objects

detected_objects = scanRadar(sector_bounderies, objects_in_area, radar)
        
print(f"Number of Detected Objects: {len(detected_objects)} | Detected Objects: {detected_objects}")
        
