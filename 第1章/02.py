# -*- encoding:utf-8 -*-

string1 = "パトカー"
string2 = "タクシー"

result = ""

for string1,string2 in zip(string1,string2):
	result += string1 + string2

print(result)