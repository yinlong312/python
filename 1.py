print("请输入最近三天登录次数")
X = input()
print("请输入最近三天发微博数")
Y = input()
X = int(X)
Y = int(Y)
if X > 20 or Y > 10 :
    print("非常活跃用户")
elif X >= 10 and X <= 20 or Y >= 5 and Y < 10 :
    print("活跃用户")
elif X < 3 and Y <= 1 :
    print("消极用户")
else :
    print("普通用户")