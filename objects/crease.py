#Class for Crease object, basically a vector wrapper

class Crease:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def make_crease(self):
        pass

    def to_string(self):
        return str(self.start[0]), str(self.start[1]), str(self.stop[0]), str(self.stop[1])

    def intyboi(self):
        sta = (int(self.start[0]), int(self.start[1]))
        sto = (int(self.stop[0]), int(self.stop[1]))

        return Crease(sta, sto)