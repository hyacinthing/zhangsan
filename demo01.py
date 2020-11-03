"""
print("holle world!") #字符串
print(2333) #整数
print(2.333) #小数
print(True) #布尔值
print(())  #元组
print([]) #数组
print({}) #字典
print("哈哈"+"嘻嘻") #字符串是拼接 哈哈嘻嘻
print("哈哈"*100)
print(2>3)
print(2<3)

#变量
#赋值
name = "张三"  #把张三这个值赋值给了名字叫a的这个变量
print(name)
"""
"""
a = input("请输入")
b = input("请输入")
print("input获取内容：",a+b)

#数字格式的转换
c = type(2333)
print(c)
"""
"""
#数字格式的转换
print(type("哈哈"))
print(type(2333))
print(type(2.333))
print(type(()))
print(type([]))
print(type({}))
"""
"""
a = (float(input("请输入")))
b = (float(input("请输入")))
print("input获取内容：",a+b)
"""
"""
a = 'dasdasdasfbui  dashduiewvyiuqe'
print(len(a))
"""
"""
a = (input("请输入"))
b = (input("请输入"))
c = print("input获取内容：",len(a+b))
"""
"""
my_list=[[1,2,3]]*3 
my_list[1][0]=100 
print(my_list)
"""
my_list = [3, 1, 2, 5, 6, 0]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
