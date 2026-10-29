money = float(input("请输入你的月收入:"))

golder = money - 5000
if golder <= 0:
  base = 0
elif golder <= 3000:
  base = golder * 0.03
elif golder > 3000 and golder <= 12000:
  base = golder * 0.10 - 210
elif golder > 12000 and golder <= 25000:
  base = golder * 0.20 - 1410
elif golder > 25000:
  base = golder * 0.25 - 2660
print(f'应缴个人所得税{base:.2f}元')