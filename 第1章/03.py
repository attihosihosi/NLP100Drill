# -*- encoding:utf-8 -*-

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

result = string.replace("," , "").replace("." , "").split()

result.sort(key=len)
result.reverse()

print(result)



