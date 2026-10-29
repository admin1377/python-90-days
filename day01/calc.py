num1 = int(input("请输入的一个数:"))
num2 = int(input("请输入第二个数:"))
calc1 = input("请输入运算符+,-,*,/:")
if calc1 == "+":
  print(f"{num1 + num2}")
elif calc1 == '-':
  print(f"{num1 - num2}")
elif calc1 == '*':
  print(f"{num1 * num2}")
elif calc1 == '/':
  if num2 == 0:
    print("除数不能为0")
  print(f'{num1 / num2}')