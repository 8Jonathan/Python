n = int(input("请输入一个正整数："))

while n > 0:
    # 判断 n 是否可以被 2 整除 #
    if n % 2 == 0:
        
        print(n,'/2 = ',n//2,sep='')
        # 按题目要求打印输出 #
        # 如果能够被 2 整除，应该写什么表达式？#
        n = n//2
    else:
        # 按题目要求打印输出 #
        print(n,'*3+1 = ',n*3+1,sep='')
        # 如果不能被 2 整除，应该写什么表达式？#
        n = n*3+1
    if n == 1:
        break

