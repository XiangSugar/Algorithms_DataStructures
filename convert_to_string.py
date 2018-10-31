# coding = utf-8
# 2018-10-20  22:07

'''
    使用递归方法来进行进制转换
    将一个十进制整数转换为1-16进制之间的任意一种进制表达形式
    并且将结果以字符串的形式返回
'''

def my_convert_to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if base > n:
        return convert_string[n]
    else:
        return my_convert_to_str(n//base, base) + convert_string[n%base]

def main():
    print("二进制：   " + my_convert_to_str(1453, 2))
    print("八进制：   " + my_convert_to_str(1453, 8))
    print("十进制：   " + my_convert_to_str(1453, 10))
    print("十六进制： " + my_convert_to_str(1453, 16))

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------

# 栈帧： 实现递归
# import Stack

# r_stack = Stack()
# def to_str(n, base):
#     convert_string = "0123456789ABCDEF"
#     while n > 0:
#         if n < base:
#             r_stack.push(convert_string[n])
#         else:
#             r_stack.push(convert_string[n % base])
#         n = n // base
#     res = ""
#     while not r_stack.is_empty():
#         res = res + str(r_stack.pop())
#     return res

# def main():
#     print("二进制：   " + to_str(1453, 2))
#     print("八进制：   " + to_str(1453, 8))
#     print("十进制：   " + to_str(1453, 10))
#     print("十六进制： " + to_str(1453, 16))

# if __name__ == '__main__':
#     main()
#-------------------------------------------------------------------------
