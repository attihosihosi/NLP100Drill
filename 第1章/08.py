# -*- encoding:utf-8 -*-
#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(str):
    tmp = u""
    for i in str:
        #小文字だったらってことなんだけどislowerのほうが賢かった　カス乙
        if i in [chr(i) for i in range(ord('a'), ord('z')+1)]:
            tmp += chr(219 - ord(i))
        else:
            tmp += i
    return tmp

string = "abcDEF"

print("before : " + string)
print("cipher : " + cipher(string))

string = "the cake is a lie"

print("before : " + string)
print("cipher : " + cipher(string))
