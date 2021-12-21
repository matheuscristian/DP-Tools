class Message():
    def __init__(self, path: str):
        self.path = path;

    def write(self, s: str):
        txt = open(self.path, "w")
        txt.write(s)

    def read(self):
        return open(self.path, "r").readline()