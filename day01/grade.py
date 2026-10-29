grade = int(input("请输入1-100之间的数字:"))
if 0 < grade or grade >0:
  print("输入错诶")
elif grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
