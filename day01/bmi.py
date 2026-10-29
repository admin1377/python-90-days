kg = float(input("请输入你的体重kg:"))
height = float(input("请输入你的身高m:"))
bmi = kg / (height * height)
if bmi < 18.5:
  print("偏瘦")
elif bmi > 18.5 or bmi <= 23.9:
  print("正常")
elif bmi > 24.0 or bmi <= 27.9:
  print("超重")
else:
  print("肥胖")