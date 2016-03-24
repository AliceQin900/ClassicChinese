#coding=utf-8
'''
Created on 2016年3月23日

@author: Administrator
'''

xingRongCi = ['Ag', 'a', 'ad', 'an']
fuCi = ['dg', 'd']
mingci = ['an', 'n', 'Ng']
lianCi = ['c']
tanCi = ['e']
fangWeiCi = ['f']
shuCi = ['m']
renMing = ['nr']
diMing = ['ns']
jieCi = ['p']
liangCi = ['q']
daiCi = ['r']
shijianCi = ['t']
zhuCi = ['u']
dongCi = ['v', 'vg', 'vd', 'vn']
yuQiCi = ['y']
zhuanYouMingCi = ['nz']


#===============================================================================
# get the corresponding chinese names of the labels
#===============================================================================
def getMapedJiebaPos(pos):
    if pos in xingRongCi:
        pos = '形容词'
    elif pos in fuCi:
        pos = '副词'
    elif pos in mingci:
        pos = '名词'
    elif pos in lianCi:
        pos = '连词'
    elif pos in tanCi:
        pos = '叹词'
    elif pos in fangWeiCi:
        pos = '方位词'
    elif pos in shuCi:
        pos = '数词'
    elif pos in renMing:
        pos = '人名'
    elif pos in diMing:
        pos = '地名'
    elif pos in jieCi:
        pos = '介词'
    elif pos in liangCi:
        pos = '量词'
    elif pos in daiCi:
        pos = '代词'
    elif pos in shijianCi:
        pos = '时间词'
    elif pos in zhuCi:
        pos = '助词'
    elif pos in dongCi:
        pos = '动词'
    elif pos in yuQiCi:
        pos = '语气词'
    elif pos in zhuanYouMingCi:
        pos = '专有名词'
    return pos


def getJiebaPosDict(jiebaDictFile):
    jiebaPosDict = {}
    handle = open(jiebaDictFile)
    for line in handle:
        entry = line.strip().split()
        term = entry[0]
        pos = entry[2]
        pos = getMapedJiebaPos(pos)
        jiebaPosDict[term] = pos
    return jiebaPosDict




