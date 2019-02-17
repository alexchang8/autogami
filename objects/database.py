class Database
    #later can implement autocomplete using a parallel data structure for only names?

    def init(self):
        self.patterns = {}

    def add(self, name, pattern):
        self.patterns[name] = pattern

    def get(self, name):
        return self.patterns.get(name)


