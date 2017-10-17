# -*- encoding:utf-8 -*-
#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
import random

#random.shuffleのまるぱくりしてちょっと変えた
def shuffle(x):
    for i in reversed(range(1, len(x)-1)):
        j = int(random.random() * (i))+1
        x[i], x[j] = x[j], x[i]
    return x

def Typoglycemia(string):
    words = string.split()
    tmp = []
    
    #これ以下の単語は並び替えない
    min_word = 4
    
    #単語に分解してからシャッフル.リストに格納
    for i in words:
        if min_word < len(i):
            tmp += ["".join(shuffle(list(i)))]
        else:
            tmp += [i]
    #リストを文字列に変換して返す
    return " ".join(tmp)

string = u"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(u"raw:" + str(string))
#raw:I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .
print(u"Typ:" + str(Typoglycemia(string)))
#Typ:I c'uondlt believe that I could ataclluy unerdtsand what I was rdaieng : the pehonneaml poewr of the hmaun mind .
#Typ:I cound'lt bveelie that I colud atucllay unadenrstd what I was ridenag : the ponnmehael pwoer of the hmuan mind .
#Typ:I cnuold't bvleiee that I culod aalutlcy utdennrsad what I was renaidg : the pnamoehenl pewor of the hmaun mind .

