#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''
from Common.langconv import *
from Dictionary.GetHanFuYinTerms import getHanFuYinTerms
from Common.PickleData import getPickleData, writePickleData
from Common.JiebaDictUtils import getJiebaPosDict

      

def predictHanFunYinPos(hanFuYinDict, jiebaPosDict):
    predictedCount = 0
    for term in hanFuYinDict.keys():
        termJian = Converter('zh-hans').convert(term.decode('utf-8'))    # 繁体-->简体
        termJian = termJian.encode('utf-8')
        if jiebaPosDict.has_key(termJian):
            hanFuYinDict[term] = jiebaPosDict[termJian]
            predictedCount += 1
    print 'pos predicted count for FuYin terms: ' + str(predictedCount)
    print 'total count of FuYin terms: ' + str(len(hanFuYinDict.keys()))
    percentage = 1.0 * predictedCount / len(hanFuYinDict.keys())
    print 'predicted percentage: ' + str(percentage)
    return hanFuYinDict




if __name__=='__main__':  
    #-----------------------------------------汉语大词典（复音词词典）------------------------------------- 
    hanFuYinFilePath = '../data/自动标注材料/词典/汉语大词典（复音词词典）/汉语大词典（第一版）词头.txt'
    label = '复音词'
    hanFuYinDict =  getHanFuYinTerms(hanFuYinFilePath, label)
    jiebaDictFile = '../data/result/jieba/dict.txt'
    jiebaPosDict = getJiebaPosDict(jiebaDictFile) 
    hanFuYinDict = predictHanFunYinPos(hanFuYinDict, jiebaPosDict)
    
    hanFuYinDictPredictFile = '../data/result/hanFuYin_PosDict_predict.pkl'
    writePickleData(hanFuYinDict, hanFuYinDictPredictFile) 
    
    
    
    
    
    
    

