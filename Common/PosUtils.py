#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''
from Dictionary.GetHanClassifedTerms import getClassifiedTerms
from Dictionary.GetHanFuYinTerms import getHanFuYinTerms
from Dictionary.GetQinJianDanYin import getQinJianDanYinTerms
from Dictionary.GetHanDanYin import getHanDanYinTerms
from Common.PickleData import getPickleData, writePickleData


posNamesMap = {'兼':'兼词', '数':'数词','介':'介词', '叹':'叹词', '副':'副词', '助':'助词', '代':'代词', '名':'名词',
               '语助':'语气助词', '动':'动词', '连':'连词', '形':'形容词', '量':'量词', '象':'象声词'}

def getPosSet(termsDict):
    posDict = {}
    for term in termsDict.keys():
        posList = termsDict[term].keys()
        for pos in posList:
            posDict.setdefault(pos, 0)
            posDict[pos] += 1
    return posDict

def getPosUnion(posDictList):
    posUnion = {}
    for posDict in posDictList:
        for pos in posDict.keys():
            posUnion.setdefault(pos, 1)
    return posUnion


def unifyPosNames(hanDanYinDict, posNamesMap):
    unifiedPosDict = {}
    for term in hanDanYinDict.keys():
        for pos in hanDanYinDict[term].keys():
            if posNamesMap.has_key(pos):
                unifiedPosDict.setdefault(term, {})
                posName = posNamesMap[pos]
                count = hanDanYinDict[term][pos]
                unifiedPosDict[term][posName] = count
    return unifiedPosDict
    

def normalizePosCount(posDict):
    for term in posDict.keys():
        totalCount = sum(posDict[term].values())
        for pos in posDict[term].keys():
            posDict[term][pos] = 1.0 * posDict[term][pos] / totalCount
    return posDict


if __name__=='__main__':
    #-----------------------------------------秦简库上网（单音1）-------------------------------------  
    qinJianDanYinFilePath = '../data/自动标注材料/词典/秦简库上网（单音词词性标注1）/单音词词性.txt'
    qinJianDanYinDict = getQinJianDanYinTerms(qinJianDanYinFilePath)
    qinJianPosDict = getPosSet(qinJianDanYinDict)
    
    #-----------------------------------------古汉语常用字字典（单音2）-------------------------------------  
    hanDanYinFilePath = '../data/自动标注材料/词典/古汉语常用字字典（单音词词性标注2）/单字词性表.txt'
    hanDanYinDict = getHanDanYinTerms(hanDanYinFilePath) 
    hanDanYinDictU = unifyPosNames(hanDanYinDict, posNamesMap) 
    hanDanYinPosDict = getPosSet(hanDanYinDictU) 
    
    posDictList = [qinJianPosDict, hanDanYinPosDict]
#     posUnion = getPosUnion(posDictList)
    posUnionFile = '../data/result/posUnionDict.pkl'
#     writePickleData(posUnion, posUnionFile) 
    posUnion = getPickleData(posUnionFile)
    for pos in posUnion.keys():
        print pos
    
    
    
