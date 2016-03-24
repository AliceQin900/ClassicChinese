#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')    # 加上这三行，解决console输出中文时编码错误
from Common.PickleData import getPickleData, writePickleData
from chardet import detect
from Common.GetPosDictionary import getTermPosDict
from Common.langconv import *
import random
import re
import jieba
jieba.load_userdict("../data/result/mergedDictionary.txt")


HAN_ZI = re.compile(r'[\x80-\xff]{3,}')   # 汉字的utf-8编码
PUNCTUATION = re.compile(ur"[\uFB00-\uFFFDh]+") # 中文标点的unicode编码  
symbolList = ['。','▓', '?', '…', '、', '●', '■', '○', '', '“', '”', '【', '】', '•', '□', '◇']


#===============================================================================
# get a term's common pos (动词，名词....) by the probability distribution
#===============================================================================
def getCommonPosByProbs(termPosProbs):
    sortedList = sorted(termPosProbs.iteritems(), key = lambda d : d[1]) # sort the values in descending order
    posList = list()
    probList = list()
    for posProb in sortedList:
        pos = posProb[0]
        prob = posProb[1]
        posList.append(pos)
        probList.append(prob)
    # calculate the accumulated probs
    sumProbList = [0]
    for i in range(0, len(probList)):    
        index = len(sumProbList)       
        sumProbList.append(sumProbList[index - 1] + probList[i])
    
    randomValue = random.random()
    for i in range(0, len(sumProbList) - 1):
        if sumProbList[i] < randomValue <= sumProbList[i + 1]:
            pos = posList[i]
            break
    return pos
        
     
#===============================================================================
# 
#===============================================================================
def getTermPos(term, classicPosDict, jiebaPosDict):
    termPos = ''
    term = term.encode('utf-8')
    if classicPosDict.has_key(term):
        posProbs = classicPosDict[term]
        posList = posProbs.keys()
        if len(posList) == 1:  #可能是: 1. 分类词 2. 复音词 3. 只有一种词性的单音词
            pos = posList[0]  
            if pos == '复音词': # 2. 复音词(后期调整词性标注）               
                termPos = '名词'
            else:                             
                termPos = pos # 1. 分类词 和  3. 只有一种词性的单音词
        else:
            termPos = getCommonPosByProbs(posProbs)  # 说明是有多种词性的单音词，按照概率分布标注词性
    else:
        termJian = Converter('zh-hans').convert(term.decode('utf-8'))    # 繁体-->简体
        termJian = termJian.encode('utf-8')
        if jiebaPosDict.has_key(termJian):
            termPos = jiebaPosDict[termJian]
        else:
            term1 = term.decode('utf-8')
            if PUNCTUATION.match(term1) or not HAN_ZI.match(term):
                termPos = '标点（符号）'
            elif term in symbolList:
                termPos = '标点（符号）'
            else:
                termPos = '名词' 
    return termPos     
                  
 

def getSegPos(myStr, classicPosDict, jiebaPosDict):
    segPosList = list()
    segList = jieba.cut(myStr)
    for term in segList:
        term = term.strip()
        if term != '':
            termPos = getTermPos(term, classicPosDict, jiebaPosDict)
            segPosList.append([term, termPos])
    return segPosList
        
        


            



if __name__=='__main__':
    termPosPickleFile = '../data/result/mergedPosDictionary.pkl'   # classic pos dictionary
    addedJiebaDictFile = '../data/result/addedJiebaDict.pkl'
    classicPosDict = getPickleData(termPosPickleFile) 
    jiebaPosDict = getPickleData(addedJiebaDictFile) 
#     termPosFile = '../data/result/mergedPosDictionary.txt'
#     termPosDict = getTermPosDict(termPosFile)
  
    
    s1 = ('一牒  。十二月庚子朔丙寅，偏將軍')
    s2 = "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿"
    seg_list = jieba.cut(s1)
    print("/ ".join(seg_list))
    
    segPosList = getSegPos(s1, classicPosDict, jiebaPosDict)
    filePath = '../data/result/test.txt'
    handle = open(filePath, 'w')
    for segPos in segPosList:
        term = segPos[0]
        pos = segPos[1]
        handle.write(term + ': ' + pos + '\n')
    handle.close()
    

    
    
    
    
    