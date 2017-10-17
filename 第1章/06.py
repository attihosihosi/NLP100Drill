# -*- encoding:utf-8 -*-
#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


string1 = u"paraparaparadise"
string2 = u"paragraph"

x = {}
y = {}
result = {}

#bi-gramは2文字ずつ分けていく
n = 2

def ngram(str,n):
    #最後の先頭文字の位置がlen(str)-n+1)になるまで
    #１文字ずつずらしながらn文字とってく
    tmp = [str[i:i+n]for i in range(len(str)-n+1)]
    return tmp

#setを使うと集合になるらしい 便利!
x=set(ngram(string1,n))
y=set(ngram(string2,n))

print("x : " + str(x))
#x : {'ra', 'ad', 'se', 'ar', 'di', 'is', 'ap', 'pa'}
print("y : " + str(y))
#y : {'ra', 'ar', 'ag', 'ph', 'ap', 'pa', 'gr'}

#和集合
result[0] = x | y
print(result[0])
#{'ra', 'ad', 'se', 'ar', 'di', 'is', 'ag', 'ph', 'ap', 'pa', 'gr'}

#積集合
result[1] = x & y
print(result[1])
#{'ap', 'pa', 'ar', 'ra'}

#差集合
result[2] = x - y
print(result[2])
#{'se', 'is', 'ad', 'di'}

#seって入ってる？
print("se x :" + str("se" in x))
#se x :True
print("se y :" + str("se" in y))
#se y :False
