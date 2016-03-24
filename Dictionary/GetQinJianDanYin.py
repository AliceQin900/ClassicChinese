#coding=utf-8
'''
Created on 2016年3月21日

@author: Administrator
'''
from nltk.tag.brill import Pos
from Common.langconv import *

#===============================================================================
# get the Qin Jian Dan Yin Terms and the corresponding pos count
#===============================================================================
def getQinJianDanYinTerms(filePath):
    termsDict = {}
    uFilepath = unicode(filePath , "utf8")
    handle = open(uFilepath)
    handle.readline()  # skip the first line
    
    for line in handle:
        entry = line.strip().split('\t')
        term = entry[0]
        pos = entry[1]
        pos = Converter('zh-hans').convert(pos.decode('utf-8'))    # 繁体-->简体
        pos = pos.encode('utf-8')
        posCount = int(entry[2])
        termsDict.setdefault(term, {})
        termsDict[term][pos] = posCount
        
    print 'total terms: ' + str(len(termsDict.keys()))
    return termsDict




        

if __name__=='__main__':
    filePath = '../data/自动标注材料/词典/秦简库上网（单音词词性标注1）/单音词词性.txt'
    termsDict = getQinJianDanYinTerms(filePath)
 
#     keyList = termsDict['愛'].keys()
#     for key in keyList:
#         print key
#     print termsDict['愛'].keys()
    
    








