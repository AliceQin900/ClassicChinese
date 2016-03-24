#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''
from Dictionary.GetHanClassifedTerms import getClassifiedTerms
from Dictionary.GetHanFuYinTerms import getHanFuYinTerms
from Dictionary.GetQinJianDanYin import getQinJianDanYinTerms
from Dictionary.GetHanDanYin import getHanDanYinTerms



def mergeDictionary(hanClassifiedDictList, hanFuYinDict, qinJianDanYinDict, hanDanYinDict):
    mergedDict = {}
    duplicateCount = 0
    for hanClassifiedDict in hanClassifiedDictList:
        for term in hanClassifiedDict.keys():
            if not mergedDict.has_key(term):
                mergedDict[term] = hanClassifiedDict[term]
            else:
                duplicateCount += 1
                
    for term in hanFuYinDict.keys():
        if not mergedDict.has_key(term):
                mergedDict[term] = hanFuYinDict[term]
        else:
                duplicateCount += 1
    
    for term in qinJianDanYinDict.keys():
        if not mergedDict.has_key(term):
                mergedDict[term] = '秦简单音'
        else:
                duplicateCount += 1
    
    for term in hanDanYinDict.keys():
        if not mergedDict.has_key(term):
                mergedDict[term] = '汉单音'
        else:
                duplicateCount += 1
    
    print 'duplicate count in all dictionaries: ' + str(duplicateCount)  
    print 'total terms in merged dictionaries: ' + str(len(mergedDict.keys()))
    return mergedDict
    

def writeDictionary(mergedDict, filePath):
    handle = open(filePath, 'w')
    for term in mergedDict.keys():
        label = mergedDict[term]
        s = term + ' ' + label
        handle.write(s + '\n')
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
    hanFuYinFilePath = '../data/自动标注材料/词典/汉语大词典（复音词词典）/汉语大词典（第一版）词头.txt'
    label = '复音词'
    hanFuYinDict =  getHanFuYinTerms(hanFuYinFilePath, label) 
#-----------------------------------------秦简库上网（单音1）-------------------------------------  
    qinJianDanYinFilePath = '../data/自动标注材料/词典/秦简库上网（单音词词性标注1）/单音词词性.txt'
    qinJianDanYinDict = getQinJianDanYinTerms(qinJianDanYinFilePath) 
#-----------------------------------------古汉语常用字字典（单音2）-------------------------------------  
    hanDanYinFilePath = '../data/自动标注材料/词典/古汉语常用字字典（单音词词性标注2）/单字词性表.txt'
    hanDanYinDict = getHanDanYinTerms(hanDanYinFilePath)
      
    mergedDict = mergeDictionary(hanClassifiedDictList, hanFuYinDict, qinJianDanYinDict, hanDanYinDict)
    dictionaryFilePath =  '../data/result/mergedDictionary.txt'
    writeDictionary(mergedDict, dictionaryFilePath)
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
                
            
    