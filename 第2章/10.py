# -*- encoding:utf-8 -*-
#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．

import codecs

n = 0
f = codecs.open(r"hightemp.txt","r","utf-8")
line = f.readline()

while line:
    n+=1
    line = f.readline()
    
print(n)
#24