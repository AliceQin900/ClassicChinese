#coding=utf-8
'''
Created on 2016年3月21日

@author: Administrator
'''

def getHanFuYinTerms(filePath, label):
    termsDict = {}
    uFilepath = unicode(filePath , "utf8")
    handle = open(uFilepath)
    handle.readline()  # skip the first line
    duplicateCount = 0
    for line in handle:
        entry = line.strip().split()
        term = entry[0]
        if not termsDict.has_key(term):
            termsDict[term] = label
        else:
            print 'duplicated: ' + term
            duplicateCount += 1
    print 'duplicate count: ' + str(duplicateCount)
    print 'total count: ' + str(len(termsDict.keys()))
    return termsDict



if __name__=='__main__':
    filePath = '../data/自动标注材料/词典/汉语大词典（复音词词典）/汉语大词典（第一版）词头.txt'
    label = '复音词'
    termsDict = getHanFuYinTerms(filePath, label)





