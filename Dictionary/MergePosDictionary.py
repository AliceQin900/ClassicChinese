#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''
from Dictionary.GetHanClassifedTerms import getClassifiedTerms
from Dictionary.GetHanFuYinTerms import getHanFuYinTerms
from Dictionary.GetQinJianDanYin import getQinJianDanYinTerms
from Dictionary.GetHanDanYin import getHanDanYinTerms
from Common.MergeProbs import mergePosProb
from Common.PosUtils import normalizePosCount, unifyPosNames, posNamesMap
from Common.PickleData import getPickleData, writePickleData

#==============================================================
# output: mergedDanYinPosDict[term] =  mergedPosProb
#==============================================================
def merge_qinJianDanYin_hanDanYin(qinJianDanYinDict, hanDanYinDictU):
    mergedDanYinPosDict = {}
    qinJianDanYinDictNorm = normalizePosCount(qinJianDanYinDict)
    hanDanYinDictUNorm = normalizePosCount(hanDanYinDictU)   # U: unified pos names; Norm: normalize the pos count 
    for term in qinJianDanYinDictNorm.keys():
        mergedDanYinPosDict.setdefault(term, {}) 
        qinPosProb = qinJianDanYinDictNorm[term]
        if  hanDanYinDictUNorm.has_key(term):
            hanPosProb = hanDanYinDictUNorm[term]
            mergedPosProb = mergePosProb(qinPosProb, hanPosProb)
            mergedDanYinPosDict[term] =  mergedPosProb
        else:
            mergedDanYinPosDict[term] =  qinPosProb
    
    for term in hanDanYinDictUNorm.keys():
        if not mergedDanYinPosDict.has_key(term):   
            hanPosProb = hanDanYinDictUNorm[term]
            mergedDanYinPosDict[term] = hanPosProb
            
    return mergedDanYinPosDict     
            
        
   
def mergeAllPosDictionary(hanClassifiedDictList, hanFuYinDict, mergedDanYinPosDict):
    mergedPosDict = {} 
    for term in mergedDanYinPosDict.keys():
        mergedPosDict[term] = mergedDanYinPosDict[term]
    countDanYin = len(mergedPosDict.keys())
    print 'all DanYin terms with pos tags: ' + str(countDanYin)
                                            
    for hanClassifiedDict in hanClassifiedDictList:
        for term in hanClassifiedDict.keys():
            if not mergedPosDict.has_key(term):
                mergedPosDict[term] =  {}
                label = hanClassifiedDict[term]
                mergedPosDict[term][label] =  1
    countClassified = len(mergedPosDict.keys()) - countDanYin
    print 'all Classified terms with pos tags: ' + str(countClassified)
    
    for term in hanFuYinDict.keys():
        if not mergedPosDict.has_key(term):
            mergedPosDict[term] =  {}
            label = hanFuYinDict[term]
            mergedPosDict[term][label] =  1
    countFuYin = len(mergedPosDict.keys()) - countDanYin - countClassified
    print 'all FuYin terms: ' + str(countFuYin)
    return mergedPosDict 
            
        
def writeTermPosDict(termPosDict, termPosFile):  
    handle = open(termPosFile, 'w')
    for term in termPosDict.keys():
        handle.write(term + '-->')
        posDict = termPosDict[term]
        for pos in posDict.keys():
            prob = posDict[pos]
            handle.write(pos + ':' + str(prob) + '\t')
        handle.write('\n')
    handle.close()
    
        
                
                
                
                
                
if __name__=='__main__':
    #-----------------------------------------汉代分类词库------------------------------------- 
    hanClassifiedFileDir = '../data/自动标注材料/词典/汉代分类词库/'
    hanClassifiedFileNames = ['表_地名.txt', '表_年号.txt', '表_人名.txt', '表_虚词.txt', '表_职官.txt', '干支.txt']
    labelsList = ['地名', '年号', '人名', '虚词', '职官', '干支']
    hanClassifiedDictList = list()
    for i in range(0, len(hanClassifiedFileNames)):
        filePath = hanClassifiedFileDir + hanClassifiedFileNames[i]
        termsDict = getClassifiedTerms(filePath, labelsList[i])
        hanClassifiedDictList.append(termsDict)
    #-----------------------------------------汉语大词典（复音词词典）------------------------------------- 
#     hanFuYinFilePath = '../data/自动标注材料/词典/汉语大词典（复音词词典）/汉语大词典（第一版）词头.txt'
#     label = '复音词'
#     hanFuYinDict =  getHanFuYinTerms(hanFuYinFilePath, label) 
    
    hanFuYinDictPredictFile = '../data/result/hanFuYin_PosDict_predict.pkl'
    hanFuYinDict = getPickleData(hanFuYinDictPredictFile)
    
    #-----------------------------------------秦简库上网（单音1）-------------------------------------  
    qinJianDanYinFilePath = '../data/自动标注材料/词典/秦简库上网（单音词词性标注1）/单音词词性.txt'
    qinJianDanYinDict = getQinJianDanYinTerms(qinJianDanYinFilePath)
    
    #-----------------------------------------古汉语常用字字典（单音2）-------------------------------------  
    hanDanYinFilePath = '../data/自动标注材料/词典/古汉语常用字字典（单音词词性标注2）/单字词性表.txt'
    hanDanYinDict = getHanDanYinTerms(hanDanYinFilePath) 
    hanDanYinDictU = unifyPosNames(hanDanYinDict, posNamesMap)
     
    mergedDanYinPosDict = merge_qinJianDanYin_hanDanYin(qinJianDanYinDict, hanDanYinDictU)
    mergedPosDict = mergeAllPosDictionary(hanClassifiedDictList, hanFuYinDict, mergedDanYinPosDict)
#     termPosFile = '../data/result/mergedPosDictionary.txt'
#     writeTermPosDict(mergedPosDict, termPosFile)
    
    termPosPickleFile = '../data/result/mergedPosDictionary.pkl' 
    writePickleData(mergedPosDict, termPosPickleFile)  
#     data = getPickleData(termPosPickleFile) 
#     term = '癸未'
#     for pos in data[term].keys():      
#         print pos + ' ' + str(data[term][pos]) 
    
    
                
                
                