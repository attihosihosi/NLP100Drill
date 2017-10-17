# -*- encoding:utf-8 -*-
#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import codecs

n = 0
f = codecs.open(r"hightemp.txt","r","utf-8")
