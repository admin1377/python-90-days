a = int(input("请输入一个数:"))
b = int(input("请输入一个数:"))
c = int(input("请输入一个数:"))
max = 0
if a >= b and a >= c:
  max = a
elif b >= a and b >= c:
  max = b
else:
  max = c
print(max)
  
 