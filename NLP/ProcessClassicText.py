#coding=utf-8
'''
Created on 2016年3月23日

@author: Administrator
'''
import re
import os
from chardet import detect

from NLP.WordPosSeg import getSegPos
from Common.PickleData import getPickleData, writePickleData


TEXT_ID = re.compile(r'[\d]+')

def getLinesPerText(filePath):
    handle = open(filePath)
    handle.readline() # skip the first line
    linesPerText = {}

    for line in handle:
        entry = line.strip().split('\t')
        if TEXT_ID.match(entry[0]):
            id = int(entry[0])
            linesPerText[id] = 1
        else:
            linesPerText[id] += 1
    return linesPerText
    
    
    
def segPosClassicFile(classicFilePath, linesPerText, classicPosDict, jiebaPosDict, segPosFilePath):
    segPosFile = open(segPosFilePath, 'w')
    segPosFile.write('ID' + '\t' + '词号' + '\t' + '词' + '\t' + '词性' + '\n')
    handle = open(classicFilePath)
    handle.readline()  # skip the first line
    unknownCount = 0 
    totalCount  = 0
    fuYinCount = 0
    
    line = handle.readline()
    while line !=  '':
        entry = line.strip().split('\t')
        if TEXT_ID.match(entry[0]):
            if len(entry) == 2:
                text =  entry[1]
            else:
                text = ''
            id = int(entry[0])
            linesCount = linesPerText[id]   # get the text for each id by the lines it contains
            for i in range(0, linesCount - 1):
                line = handle.readline()
                text = text + ' ' + line.strip()
                         
            segPosList = getSegPos(text.strip(), classicPosDict, jiebaPosDict)
            for j in range(0, len(segPosList)):
                segPos = segPosList[j]
                term = segPos[0]
                pos = segPos[1]
                totalCount += 1
                if pos == '未知':
                    unknownCount += 1
                elif pos == '复音词':
                    fuYinCount += 1
                
                segPosFile.write(str(entry[0]) + '\t' + str(j + 1) + '\t' +  term + '\t' + pos + '\n')
            line = handle.readline()
    handle.close()
    segPosFile.close()
    print 'count of terms with unknown pos: ' + str(unknownCount)
#     print 'count of terms with fuYinCi pos: ' + str(fuYinCount)
    print 'total terms count: ' + str(totalCount)
                
            


  

if __name__=='__main__':
    termPosPickleFile = '../data/result/mergedPosDictionary.pkl'   # classic pos dictionary
    addedJiebaDictFile = '../data/result/addedJiebaDict.pkl'  
    classicPosDict = getPickleData(termPosPickleFile) 
    jiebaPosDict = getPickleData(addedJiebaDictFile) 
    
    classicFileDir  = unicode('../data/自动标注材料/文献库/文献总库/', "utf8")
    posFileDir = unicode('../data/自动标注材料/文献库/文献总库_词性标注/', "utf-8")
    classicFiles = os.listdir(classicFileDir)
    for f in classicFiles:
        print f
        classicFilePath = classicFileDir + '/' + f
        fileName = f.split('.')[0]
        segPosFile = fileName + '_词性标注.txt'
        segPosFilePath = posFileDir + '/' + segPosFile
        linesPerText = getLinesPerText(classicFilePath)
        segPosClassicFile(classicFilePath, linesPerText, classicPosDict, jiebaPosDict, segPosFilePath)
    
    
    
#     classicFilePath = '../data/自动标注材料/文献库/文献总库/disc新简号.txt'
#     classicFilePath = unicode(classicFilePath , "utf8")
#     segPosFilePath = '../data/自动标注材料/文献库/文献总库_词性标注/disc新简号_词性标注.txt'
#     segPosFilePath = unicode(segPosFilePath , "utf8")     
#     linesPerText = getLinesPerText(classicFilePath)    
#     segPosClassicFile(classicFilePath, linesPerText, classicPosDict, jiebaPosDict, segPosFilePath)
                   
    
                                   
                                         

                                       

             
            
                             
        
        
            
            
            
            
            
            
            
        
        
        
            
            
                
        
        
        
        
        
