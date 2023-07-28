# # string = input("Enter string:")
# # tot = " "
# # for i in string:
# #     tot = tot + i * 2
# # print(tot)
#
# list1 = [1, 2, 3, 4, 5, 6, 13, 54, 13]
# sum_num = 0
# length = len(list1)
# for i in range(length):
#     if list1[i] == 13:
#         continue
#     else:
#         sum_num = sum_num + list1[i]
#
# print(sum_num)
#
#
# num = 5
# k = num
# for i in range(num):
#     for j in range(k-i,0,-1):
#         print(j, end=" ")
#     print("\r")
#
# start = 20
# end = 50
# for i in range(20, 50):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
#
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
# for i in range(10-2):
#     fibonacci = n1 + n2
#     print(fibonacci)
#     n1 = n2
#     n2 = fibonacci
#
num = 5

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(factorial)

string="raj kumar"
# cap = string.capitalize()
cap = string.replace("r","m")
print(cap)