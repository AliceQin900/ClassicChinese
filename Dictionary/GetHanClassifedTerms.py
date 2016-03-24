#coding=utf-8
'''
Created on 2016年3月21日

@author: Administrator
'''



def getClassifiedTerms(filePath, label):
    termsDict = {}
    uFilepath = unicode(filePath , "utf8")
    handle = open(uFilepath)
    handle.readline()  # skip the first line
    duplicateCount = 0
    for line in handle:
        entry = line.strip().split()
        term = entry[1]
        if not termsDict.has_key(term):
            termsDict[term] = label
        else:
            print 'duplicated: ' + term
            duplicateCount += 1
    print 'duplicate count: ' + str(duplicateCount)
    print 'total count: ' + str(len(termsDict.keys()))
    return termsDict


if __name__=='__main__':
    fileDir = '../data/自动标注材料/词典/汉代分类词库/'
    fileNames = ['表_地名.txt', '表_年号.txt', '表_人名.txt', '表_虚词.txt', '表_职官.txt', '干支.txt']
    labelsList = ['地名', '年号', '人名', '虚词', '职官', '干支']
    
#     i = 5
#     filePath = fileDir + fileNames[i]
#     print filePath
#     termsDict = getClassifiedTerms(filePath, labelsList[i])
    
    for i in range(0, len(fileNames)):
        filePath = fileDir + fileNames[i]
        termsDict = getClassifiedTerms(filePath, labelsList[i])

        
        
        