#num = int(input("请输入一个整数:"))
user_input = input("请输入一个整数:")
#if num.isdigit():
if user_input.isdigit():
  num = int(user_input)
  if num % 2 == 1:
   print("这个数奇数.")
  else: 
   print("这个数是偶数")
else:
   print("这个数是非整数")