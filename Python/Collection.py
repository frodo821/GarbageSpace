#-*-coding:utf-8;-*-

class Collection(object):
    __clcts = dict()
    def __getid(self):
        return str(id(self))
    
    def __init__(self):
        Collection.__clcts[self.__getid()] = dict()
    
    def __getattribute__(self, name):
        try:
            return object.__getattribute__(Collection, __clcts)[self.__getid()][name]
        except IndexError:
            raise AttributeError("'Collection' object has no attribute '{}'".format(name))
    
    def __setattr__(self, name, value):
        Collection.__clcts[self.__getid()].update({name: value})
    
    def __delattr__(self, name):
        del Collection.__clcts[self.__getid()][name]
