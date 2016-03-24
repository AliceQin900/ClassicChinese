#coding=utf-8
'''
Created on 2015年11月13日

@author: Administrator
'''

import cPickle as pickle



def getPickleData(pickleFile):
    handle = open(pickleFile)
    data = pickle.load(handle)
    handle.close()
    return data


def writePickleData(data, pickleFile):
    handle = open(pickleFile, 'w')
    pickle.dump(data, handle)
    handle.close()
    
    