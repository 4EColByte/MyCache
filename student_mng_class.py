#!/usr/bin/env python
# coding=uft-8

#学生信息
class student():

    name=''

    def __init__(self, name, *args):
        self.name = name
        self.sexy = args[0]
        self. = args[1]
        self.age = args[2]
        self.addr = args[3]
        self.QQ = args[4]
    def get_info():
        return self.name, self.sexy, self.age, self.addr, self.QQ

    def update_info(*args):
        self.name = args[0]
        self.sexy = args[1]
        self. = args[2]
        self.age = args[3]
        self.addr = args[4]
        self.QQ = args[5]

    def update_info_property(property,value)
        self.property = value

    def get_info_property(property,value):
        return self.property

class file_store():

    file_name = ''

    def __init__(file_string):
        self.file_name = file_string

    def open_read():
        return open(self.file_name)

    def open_update():
        pass

   
if __name__ == '__main__':
    start()
