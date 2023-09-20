a = int(input())
b = int(input())
x=a
while x % a != 0 or x % b != 0:
    x+=1
print(x)