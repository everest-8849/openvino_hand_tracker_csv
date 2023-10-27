import csv
import math
import bpy


file = "P:/.../data/hand_track.csv"
delimiter = ','



with open(file) as csvfile:
    r = csv.reader(csvfile, delimiter=delimiter)
    for frame, row in enumerate(r):
        if (frame == 0): 
            continue            
        
        if len(row) == 0:
            continue
        

        points = [[float(coord) for coord in row[i:i+3]] for i in range(0, len(row), 3)]
        
        for pid, point in enumerate(points):
            object = bpy.data.objects[f"object_{pid}"]
            
            bpy.context.object.location = tuple(point)

            bpy.context.object.keyframe_insert(data_path="location", frame=frame)
