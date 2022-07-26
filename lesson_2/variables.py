var1 = 76
var2 = 812
print(var1, var2)

var3 = var1

var1 = var2
var2 = var3

print(var1, var2)

var1, var2 = var2, var1
print(var1, var2)