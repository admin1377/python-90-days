username = input("请输入你的用户名:")
password = input("请输入你的密码:")
if username == 'admin' and password == '123456':
  print('欢迎')
elif username == '' or password == '':
  print('不能为空白')
else:
  print("错误")