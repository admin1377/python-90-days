text = input("请输入金额:")

#整数
if not text.isdigit():
  print("请输入整数")
else:
  amount = int(text)
#小数（允许一个小数点）
if not text.replace('.','',1).isdigit():
  print("请输入数字")
else:
  amount = float(text)