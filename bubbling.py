#冒泡排序
def Bubbling(list_a):        #定义一个Bubbling函数。注意：默认参数最好不要是可变对象
    for i in range(1,len(list_a)):          #设定循环次数len()-1，使用range()函数读取len()方法返回的值
        print('第{}次排序'.format(i))       #方便查看，打印排序次数
        for j in range(len(list_a)-i):      #设定比较次数，递减，i+j=len()
            print('比较第{}次'.format(j))   #方便查看，打印比较次数
            if list_a[j] > list_a[j+1]:     #对比相邻的俩个数，若list_a[j]>list_a[j+1]，交换位置
                list_a[j],list_a[j+1] = list_a[j+1],list_a[j]       #交换相邻俩个数的位置
                print(list_a)       #打印每次交换交换位置后数组
    print(list_a)       #打印排序完成的数组
Bubbling(list_a = [9,33,5,22,32,1])     #调用Bubbling函数，使用关键字传参
print()
