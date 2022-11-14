import re

from string import Template
from os import write

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

contentStorage = Content_storage()

class Verilog_Strings():
    
    #WIP still figuring out what needs to be initialized as attribute
    def __init__(self):
        file_contents = []
        set_item_val = ""
        filename = ""

        self.file_number = set_item_val
        self.file_contents = file_contents
        self.filename = filename

    def __setitem__(self, filename, val):
        """Opens file and reads it given provided filename, all of it's contents are stored in contentStorage"""
        Verilog_Strings.set_item_val = val
        Verilog_Strings.filename = filename
        with open(filename, "r") as f:
            lines = f.readlines()
            contentStorage.append(str(lines))


        def write():
            
            #pin_numbers = [re.sub(r'\D',"" ,s) for s in contentStorage[0]]
            pin_numbers = "".join([x for x in contentStorage[0] if x in "0123456789"])
            print(pin_numbers)
        write()


    

VHDL_Replace = Verilog_Strings()
VHDL_Replace["lmao.txt"] = "0"




