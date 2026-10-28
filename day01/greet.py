name = input("请输入你的姓名")

#if name == name:       #bug错误代码
if name != '':
  print("你好!" + name)
elif name == '':
  print("你好!朋友")