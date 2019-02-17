class Pattern():

    '''
    a Pattern object has three fields:
        - name: a string describing the name of the object
        - image: a string describing filepath to image
        - creases: a list of Crease objects
        - dim: a tuple representing the dimension of the image

    '''


    def __init__(self, name, dim, image = None, creases):
        self.name = name
        self.image = image
        self.dim = dim
        self.creases = creases

    def from_image(self, img):
        #lillian


    def make_creases(self):
        for c in creases:
            c.make_crease()

