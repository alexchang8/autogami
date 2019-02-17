class Pattern:


    def __init__(self, name, dims, creases):
        self.creases = creases
        self.name = name
        self.dims = dims

    def from_image(self, img):
        #lillian
        pass


    def make_creases(self):
        for c in creases:
            c.make_crease()

