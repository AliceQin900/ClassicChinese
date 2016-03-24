#coding=utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''

#===============================================================================
# posProbDict1[pos] = prob; posProbDict2[pos] = prob
#===============================================================================
def mergePosProb(posProbDict1, posProbDict2):
    mergedPosProbDict = {}
    for pos in posProbDict1.keys():
        prob1 = posProbDict1[pos]
        if posProbDict2.has_key(pos):
            prob2 = posProbDict2[pos]
            mergedPosProbDict[pos] = (prob1 + prob2) / 2
        else:
            mergedPosProbDict[pos] = prob1 / 2
    for pos in posProbDict2.keys():
        if not mergedPosProbDict.has_key(pos):
            prob2 = posProbDict2[pos]
            mergedPosProbDict[pos] = prob2 / 2
    return mergedPosProbDict




if __name__=='__main__':
    posProbDict1 = {'动词': 0.2, '介词': 0.8}
    posProbDict2 = {'动词': 0.1, '介词': 0.3, '助词':0.6}  
    mergedPosProbDict =  mergePosProb(posProbDict1, posProbDict2)
    for pos in mergedPosProbDict.keys():      
        print pos + ': ' +  str(mergedPosProbDict[pos])







