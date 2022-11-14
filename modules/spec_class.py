class Content_storage:
    length = 0

    def __getitem__(self, key):
        return self.__getattribute__(str(key))

    def __setitem__(self, key, val):
        self.__setattr__(str(key), val)

    def __delitem__(self, key):
        self.__delattr__(key)

    def append(self, val):
        self[str(self.length)] = val
        self.length += 1
