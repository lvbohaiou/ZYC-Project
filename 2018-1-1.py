# print("abc" + "efg")
#
# while True:
#     score = int(input("请输入您的分数："))
#     if score >= 90:
#         print("优秀")
#     elif score >= 80:
#         print("良好")
#     else:
#         print("一般")

# 1 * 1 = 1
# 1 * 2 = 2 2 * 2 = 3 ... 9 * 2 = 18
# 1 * 3 = 3 2 * 3 = 6 ... 9 * 3 = 27
# 1 * 4 = 4 2 * 4 = 8 ... 9 * 4 =36
# ...
# 1 * 9 = 9 2 * 9 = 18 ... 9 * 9 =81

line = 1
number1 = 1
while line <= 9:
    while number1 <= 9:
        for i in range(1, number1+1):
            print('%d * %d = %d' % (i, line, number1 * line), end='  ')
        print()
        number1 += 1
        line += 1


