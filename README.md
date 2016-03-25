# Project : ClassicChinese

## Main functions:

### 1. Word segmentation for classic Chinese(文言文、古文)：
 1.1  config the classic Chinese dictionary
 
 1.2  invoke Jieba.cut (mystr) 
 
### 2. Part of speech (pos) tagging：
2.1 If the term is in the classic Chinese dictionary, then tag it with the corresponiding pos.  In particular, if a term has more than one pos in the dictionary, it is tagged based on the pos probability distribution. 

 2.2 Otherwise, we predict the pos based on the morden Chinese dictionary (Jieba default dictionary).

