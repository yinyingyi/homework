'''
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序
条件：（1）要有for循环；（2）要有append
'''

# 方法一：for循环
# list_a = [2,8,4,25,16]
# list_b = []
# for i in list_a:
#     list_b.append(i**2)
# print(list_b)

#方法二：列表推导式
list_a = [2,8,4,25,16]
print([i**2 for i in list_a])