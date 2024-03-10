# Identity Operator : is

x = y = [1, 2, 3]

z = [1, 2, 3]

print(x==y)
print(x==z)
print(x is y)
print(x is z)
print("***************************")
x = [1, 2, 3]
y = [2,4]
del x[2]
y[1] = 1
y.reverse()
print(x==y)
print(x is y)
print(x is not y)

print("********************")
x = ["BMW","Volvo"]
print("BMW" in x )

name ='Fehmi'
print('e' in name)
print('i'not in name)