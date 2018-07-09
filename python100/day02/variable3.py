#coding=utf-8

#使用type()检查变量的类型

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 在对变量类型进行转换时可以使用Python的内置函数（准确的说下面列出的并不是真正意义上的函数，而是后面我们要讲到的创建对象的构造方法）

# int()：将一个数值或字符串转换成整数,可以指定进制
# float()：将一个字符串转换成浮点数
# str()：将指定的对象转换成字符串形式，可以指定编码
# chr()：将整数转换成该编码对应的字符串（一个字符）
# ord()：将字符串（一个字符）转换成对应的编码（整数）