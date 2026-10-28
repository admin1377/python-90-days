date = int(input("请输入你的出生年份:"))
#if date == 1900 or  2026:
if  1900 <= date <= 2026:
  print(f"你今年岁{2026-date}")
else:
  print("输入错误，你输入的年份应该在1900和2026之间")