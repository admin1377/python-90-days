kg = int(input("请输入货物重量:"))
money = float(input("请输入订单金额:"))
area = input("是否偏远(y/n)").strip().lower() == "y"
amount = input("是否会员(y/n)").strip().lower() == "y"

if kg <= 1:
  base = 10
elif kg <= 3:
  base = 15
elif kg <= 5:
  base = 20
elif kg > 5:
  base = 25 + (kg - 5) * 2
remote_fee = 5 if area else 0
if   amount:
  if money >= 99:
    fee = 0
  else:
    fee = base * 0.5 + remote_fee
else:
  fee = base + remote_fee
print(f"运费{fee:g}元")
  

