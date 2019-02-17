import math
class Gcode:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern
        self.scale = 150 / pattern.dims[1]

    def to_string_list(self):
        gcode = []
        #gcode.append("G28 X Y Z") #move the printer head to home
        gcode.append("G28 X Y")
        gcode.append("G91")
        gcode.append("G1 Z10") #move the print head up       
        for crease in self.pattern.creases:
            sp1 = (str(crease.start[0]*self.scale + 5), str(crease.start[1]*self.scale + 5))
            sp2 = (str(crease.stop[0]*self.scale + 5), str(crease.stop[1]*self.scale + 5))
            gcode.append("G90")
            gcode.append("G1 " + "X" + sp1[0] + " Y" + sp1[1] + " F2000") #move the stopprint head to p1
            gcode.append("G91")
            gcode.append("G1 Z-10") #move the print head down
            gcode.append("G90")
            gcode.append("G1 " + "X" + sp2[0] + " Y" + sp2[1] + " F100") #move the print head to p2
            gcode.append("G91")
            gcode.append("G1 Z10") #move the print head up
        #gcode.append("") #home the printer again and cleanup?
        return gcode