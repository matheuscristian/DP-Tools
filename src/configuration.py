class Config:
    def __init__(self, path: str) :
        self.path = path
        
        self.config = {}

        configR = open(self.path, "r").readlines()
        for data in configR:
            try:
                values = data.split("=")
                self.config[values[0].strip("\n")] = values[1]
            except:
                pass

    def getValue(self, key: str):
        return self.config[key]

    def setValue(self, key: str, value):
        self.config[key] = value

    def writeConfig(self):
        configW = open(self.path, "w")
        txt = ""
        for item in self.config:
            txt += item + "=" + self.config[item] + "\n"
        configW.write(txt)
        configW.close()