class Memory:
    def __init__(self):
        self.__mem = set()

    def add(self, key, value):
        self.__mem.add({key: value})

    def get(self, key):
        for i in self.__mem:
            if key in [j for j in i]:
                return i
