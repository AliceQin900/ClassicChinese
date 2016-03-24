Project : ClassicChinese

Main functions:

1.  word segmentation for the classic Chinese(文言文、秦简、汉书等）：
（1）config the classic Chinese dictionary
（2）invoke Jieba.cut(mystr) 
	
2. part of speech (pos) tagging：
（1）If the term is in the classic Chinese dictionary, then tag it with the corresponiding pos.
( Note : If a term has more than one pos, then get the pos based on the pos probability distribution)

（2）Otherwise, predict the pos based on the morden Chinese dictionary (Jieba default dictionary).