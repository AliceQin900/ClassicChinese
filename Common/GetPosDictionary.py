#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''



def getTermPosDict(termPosFile):
    termPosDict = {}
    handle = open(termPosFile)
    for line in handle:
        entry = line.strip().split('-->')
        term = entry[0]
        termPosDict.setdefault(term, {})
        posProbStrList = entry[1].split('\t')
        for posProbStr in posProbStrList:
            posProb = posProbStr.split(':')
            pos = posProb[0]
            prob = float(posProb[1])
            termPosDict[term][pos] = prob
    return termPosDict
            


if __name__=='__main__':
    termPosFile = '../data/result/mergedPosDictionary.txt'
    termPosDict = getTermPosDict(termPosFile)
    print len(termPosDict.keys())
    
    term = '今'
    for pos in termPosDict[term].keys():
        print pos + ': ' + str(termPosDict[term][pos])
    











