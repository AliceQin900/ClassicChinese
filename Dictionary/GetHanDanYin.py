#coding=utf-8
'''
Created on 2016年3月21日

@author: Administrator
'''
import re
from chardet import detect


POS_NUMBER = re.compile(r'[\d]+')
HAN_ZI = r'[\x80-\xff]{3}'   # 1个汉字的utf-8编码
POS_TEXT1 = re.compile(r'〈([\x80-\xff]{3,6})〉.*')  # 词性名称含有1-2个汉字， 所以{3, 6}
POS_TEXT2 = re.compile(r'<([\x80-\xff]{3,6})>.*')



def extractPosName(posText):
    posText = posText.strip()
    posName = ''
    match1 = POS_TEXT1.match(posText)
    if match1:
        posName = match1.group(1)
    else:
        match2 = POS_TEXT2.match(posText)
        if match2:
            posName = match2.group(1)
    return posName
  
    
#===============================================================================
# get the Han Dan Yin Terms and the corresponding pos count
#===============================================================================
def getHanDanYinTerms(filePath):
    termsDict = {}
    uFilepath = unicode(filePath, "utf8")
    handle = open(uFilepath)
    handle.readline()  # skip the first line
    
    for line in handle:
        entry = line.strip().split('\t')
        term = entry[0]
        text = entry[1]
        termsDict.setdefault(term, {})
        oneline = text.replace('\n', ' ')
        posTextList = POS_NUMBER.split(oneline)
        for posText in posTextList:
            posName = extractPosName(posText)
            if posName != '':
                termsDict[term].setdefault(posName, 0)
                termsDict[term][posName] += 1
    return termsDict
            
            




     


if __name__=='__main__':
#     text = '''1〈名〉山陵；大丘。王勃《滕王阁序》：“访风景于崇～。”2<语助>山湾。屈原《山鬼》：“若有人兮山之～。”3〈名〉屋角翘起来檐。《古诗十九首·西北有高楼》：“～阁三重阶。”4〈动〉曲从；迎合。《韩非子·有度》：“法不～贵，绳不挠曲。”（贵，地位高的人。）5〈动〉偏私；袒护。屈原《离骚》：“皇天无～私兮。”〖引〗亲近。《后汉书·文苑传下》：“苟失其道，则兄弟不～。”6通“婀”。柔软而美丽的样子。《诗经·小雅·隰桑》：“隰桑有～，其叶有难。”（难，茂盛的样子。）'''
#     oneline = text.replace('\n', ' ')
# 
#     textList = POS_NUMBER.split(oneline)
#     for l in textList:
# #         print l
#         match1 = POS_TEXT1.match(l.strip())
#         if match1:
#             print match1.group(1)
#         else:
#             match2 = POS_TEXT2.match(l.strip())
#             if match2:
#                 print match2.group(1)

    filePath = '../data/自动标注材料/词典/古汉语常用字字典（单音词词性标注2）/单字词性表.txt'
    termsDict = getHanDanYinTerms(filePath) 
    term = '做'
    print term
    posDict = termsDict[term]
    for pos in posDict.keys():
        print pos + ': ' + str(posDict[pos])
    
            
        

    
    
    
    
    
    
    
    
    
    