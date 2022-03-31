
class Config:
    def __init__(self, map: dict):
        self.properties = map

    def get_property(self, name: str):
        return self.properties.get(name)


def parse(filename: str):
    properties = {}
    file = open(filename, 'r')

    while (line := file.readline()) != '':
        split: str = line.__str__().split("=")
        key = split[0].strip()
        value = split[1].strip()
        properties[key] = value
    return Config(properties)

