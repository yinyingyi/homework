
class Community:    #定义Community类
    area = 10000    #定义静态变量
    print("类一：Community类")  #输出类名，方便查看代码运行结果

    def __init__(self):         #定义私有方法
        shape_hill = "round"    #定义私有属性shape_hill
        game_room = "big"       #定义私有属性game_room
        print(f"我们的社区占有{shape_hill}形状的假山,还有非常{game_room}的游戏室")

    def flower_color(self,color1,color2,flower):    #定义公用方法
        #定义变量值,加self后可被其他变量调用，否则无法调用
        self.color1 = color1
        self.color2 = color2
        self.flower = flower

        # 条件判断
        if self.flower == "牡丹":     # 如果有牡丹，输出社区有color1的flower
            print(f"社区有{self.color1}{self.flower}")
        else:                           # 否则，输出社区有color2的flower
            print(f"社区有{self.color2}{self.flower}")
co = Community()    #对类进行实例化
co.flower_color("白色","粉色","牡丹")         #给flower_color传参
co.flower_color("白色","粉色","玫瑰")         #给flower_color传参
co.flower_color("白色","粉色","康乃馨")        #给flower_color传参
print(f"社区占地面积{co.area}平米")             #输出社区面积
print()     #输出空白行，方便查看代码运行结果



class SdHospital:               #定义Hospital类
    print("类二：Hospital类")   #输出类名，方便查看代码运行结果

    def courtyard_area(self,ar_name,ar_type,address):    #定义院区方法
        self.ar_name = ar_name          #定义院区属性——院区名称
        self.ar_type = ar_type          #定义院区属性——院区类型
        self.address = address          #定义院区属性——院区地址

    def department(self,de_name,de_type):       #定义科室方法
        affiliated_hospital = self.ar_name      #定义科室属性——科室所属院区，获取courtyard_area方法里ar_name值
        self.de_name = de_name      #定义科室属性——科室名称
        self.de_type = de_type      #定义科室属性——科室类型

    def doctor(self,do_name,good_at):           #定义医生方法
        affiliated_department = self.de_name    #定义医生属性——所属科室
        self.do_name = do_name                  #定义医生属性——医生名称
        self.good_at = good_at                  #定义医生属性——医生擅长方向

        #判断语句
        if self.ar_type == "三甲":    #如果医院类型是三甲，输出医院科室医生信息
            print(f"医院名称：{self.ar_name}、类型：{self.ar_type}、地址：{self.address}")
            print(f"科室名称：{self.de_name}、类型：{self.de_type}")
            print(f"医生姓名：{self.do_name}、擅长：{self.good_at}")
            print()
        elif self.ar_type == "二乙":  #如果医院类型是二乙，输出科室信息
            print(f"{self.ar_name}等级太低，只有科室名称：{self.de_name}、类型：{self.de_type}就好")
            print()
        else:   #其他条件下，输出医生信息
            print(f"{self.ar_name}太低级了，只有{self.de_name}的{self.do_name}医生凑数{self.good_at}")

sdhos = SdHospital()    #对类进行实例化
#给医院、科室、医生方法传参
sdhos.courtyard_area("医大附属医院","二乙","山东省青岛市")
sdhos.department("骨科","热门科室")
sdhos.doctor("张大夫","胳膊腿")

sdhos.courtyard_area("齐鲁医院","三甲","山东省济南市")
sdhos.department("神经科","热门科室")
sdhos.doctor("李时珍","望闻问切")

sdhos.courtyard_area("妇幼保健院","一乙","山东省曲阜")
sdhos.department("外科","普通科室")
sdhos.doctor("李静静","实际啥都不擅长")
print()     #输出空白行，方便查看代码运行结果


class SuperMarket():                #定义SuperMarket类
    print("类三：SuperMarket类")    #输出类名，方便查看代码运行结果
    def __init__(self,glass= "杯子",scoop="勺子"):         #定义私有方法，并给属性赋默认值
        self.glass = glass
        self.scoop = scoop
    def vegetables_price(self,number,egg,potato,spinach):   #定义蔬菜价格方法
        self.number = number        #定义属性——数量
        self.egg = egg              #定义属性——鸡蛋
        self.potato = potato        #定义属性——土豆
        self.spinach = spinach      #定义属性——菠菜
        # 输出今日购买蔬菜单价和数量
        print("今日买了{}份菜，其中每份鸡蛋{}元、土豆{}元、菠菜{}元".format(number,egg,potato,spinach))
    def fruits_price(self,apple,orange,cherry):     #定义水果方法
        self.apple = apple          #定义属性——苹果
        self.orange = orange        #定义属性——橘子
        self.cherry = cherry        #定义属性——樱桃
        print("今日苹果{}元、橘子{}元、樱桃{}元".format(apple,orange,cherry))    #输出今日购买水果单价
    def activity(self):         #定义活动方法
        price1 = self.number * (self.egg + self.potato + self.spinach)      #定义蔬菜总价，并获取vegetables_price里的属性值
        price2 = self.apple + self.orange + self.cherry                     #定义水果总价，并获取fruits_price里的属性值

        #判断语句
        if price1 > price2:         #如果蔬菜价格>水果价格，赠送一个杯子
            # 输出价格，并获取私有属性里的glass值
            print("蔬菜共计{}元、水果共计{}元,所以送您一个{}".format(price1,price2,self.glass))
        elif price1 == price2:      #如果蔬菜价格=水果价格，赠送一个勺子
            # 输出价格，并获取私有属性里的scoop值
            print("蔬菜共计{}元、水果共计{}元,所以送您一个{}".format(price1,price2,self.scoop))
        else:   #其他，不赠送
            print("买的太少，啥都不送")

sup = SuperMarket()     #对类进行实例化
sup.vegetables_price(5,4,2,1.5)     #给vegetables_price传参
sup.fruits_price(1,2,44)        #给fruits_price传参
sup.activity()  #调用类activity方法
print()     #输出空白行，方便查看代码运行结果


class Star():                   #定义Star类
    print("类四：Star类")       #输出类名，方便查看代码运行结果
    def generality(self,track,isotropy,coplanarity):    #定义星球共同特性generality方法
        self.track = track                  #定义属性——轨道
        self.isotropy = isotropy            #定义属性——同向性
        self.coplanarity = coplanarity      #定义属性——共面性

    def earth(self):        #定义地球方法
        atmosphere = 'atmosphere'       #定义地球属性
        #输出地球所有特性，获取generality方法里的属性值
        print("地球的特性：除了{}、{}、{}，地球还有{}".format(self.track,self.isotropy,self.coplanarity,atmosphere))

    def moon(self):     #定义月球方法
        characteristic = 'Lunar eclipse'    #定义月球属性
        # 输出月球所有特性，获取generality方法里的属性值
        print("月球的特性：除了{}、{}、{}，月球还有{}现象".format(self.track,self.isotropy,self.coplanarity,characteristic))

s = Star()      #对类进行实例化
s.generality('circular','Same direction','Coplanar')    #给generality方法传参
s.earth()       #调用类earth方法
s.moon()        #调用类moon方法
print()     #输出空白行，方便查看代码运行结果



class Person():                 #定义Person类
    print("类五：Person类")     #输出类名，方便查看代码运行结果
    def attribute(self,name):   #定义人的特点方法
        self.name = name    #定义属性——姓名

    def student(self,achievement = 58):      #定义学生方法,并给成绩赋默认值
        #使用while循环输出成绩，直到成绩及格
        while achievement < 60:
            print("{}的成绩是{}，不及格，要加油哦!".format(self.name,achievement))
            achievement += 1    #成绩+1，继续根据条件循环
        else:
            print("{}的成绩是{}，恭喜你及格了！".format(self.name,achievement))

    def worker(self):   #定义工人方法
        merits = ''     #定义绩效属性，并赋空值
        for merits in range(8,11):  #使用for循环输出绩效结果
            if merits == 8:
                print("{}的一季度绩效是{}，等级是C".format(self.name,merits))
            elif merits == 9:
                print("{}的二季度绩效是{}，等级是B".format(self.name,merits))
            else:
                print("{}的三季度绩效是{}，等级是A".format(self.name,merits))

p = Person()        #对类进行实例化
p.attribute('Tom')  #给attribute方法传参
p.student()         #调用类student方法
p.worker()          #调用类worker方法