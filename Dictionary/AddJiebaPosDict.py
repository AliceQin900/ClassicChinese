#coding=utf-8
'''
Created on 2016年3月23日

@author: Administrator
'''

from Common.langconv import *
from Common.JiebaDictUtils import getJiebaPosDict
from Common.PickleData import getPickleData, writePickleData




#===============================================================================
# convert the terms in rawPosDict to jian ti
#===============================================================================
def getJianTiClassicPosDict(classicPosDict):
    jianClassicPosDict = {}
    for term in classicPosDict.keys():
        termJian = Converter('zh-hans').convert(term.decode('utf-8'))    # 繁体-->简体
        termJian = termJian.encode('utf-8')
        jianClassicPosDict[termJian] = classicPosDict[term]
    return jianClassicPosDict
        
    

#===============================================================================
# rawPosDict: classic chinese dictionary
#===============================================================================
def addJiebaPosDict(jiebaPosDict, jianClassicPosDict):
    addedPosDict = {}
    for term in jiebaPosDict.keys():
        if len(term) <= 10:   # 只取不超过5个汉字的词加入posDict (一个汉字长度为2)
            if not jianClassicPosDict.has_key(term):
                addedPosDict[term] = jiebaPosDict[term]          
    return addedPosDict




if __name__=='__main__':
    jiebaDictFile = '../data/result/jieba/dict.txt'
    termPosPickleFile = '../data/result/mergedPosDictionary.pkl'
    
    classicPosDict = getPickleData(termPosPickleFile) 
    jianClassicPosDict = getJianTiClassicPosDict(classicPosDict) 
    jiebaPosDict = getJiebaPosDict(jiebaDictFile) 
    
    addedPosDict = addJiebaPosDict(jiebaPosDict, jianClassicPosDict)
    print len(addedPosDict.keys())
    
    addedJiebaDictFile = '../data/result/addedJiebaDict.pkl'
    writePickleData(addedPosDict, addedJiebaDictFile)
    
    











       
            
    
    