# -*- encoding:utf-8 -*-

#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

string = u"I am an NLPer"

result = {}

#bi-gramは2文字ずつ分けていく
n = 2

def ngram(str,n):
    #最後の先頭文字の位置がlen(str)-n+1)になるまで
    #１文字ずつずらしながらn文字とってく
    tmp = [str[i:i+n]for i in range(len(str)-n+1)]
    return tmp

#単語bi-gramの結果
result = ngram(string,n)   
print (result)
#['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

#文字bi-gramの結果
result = ngram(string.split(),n)
print(result)
#[['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
