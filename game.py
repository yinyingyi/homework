'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
希望各位同学在此基础上可以添加自己的“freestyle”哦
'''
import random       #引入random()函数
hp = [1000,1200,1500,1600]      #定义血量hp的随机值范围
power1 = [10,20,30,50]          #定义童姥武力值power1的随机值范围
power2 = [220,350,470,600]      #定义敌人武力值power2的随机值范围
mp = [1,1.2,1.4,1.6]            #定义魔力值mp的随机值范围

class Tonglao():            #定义Tonglao类
    def __init__(self):     #定义私有方法
        self.hp = random.choice(hp)         #定义童姥属性——血量，使用choice()函数随机返回一个值
        self.power = random.choice(power1)  #定义童姥属性——武力值（攻击力），使用choice()函数随机返回一个值
        self.mp = random.choice(mp)         #定义童姥属性——魔力值，使用choice()函数随机返回一个值

    def see_people(self,name):      #定义see_people方法
        self.name = name            #定义name属性
        print("童姥看到的人是{}".format(self.name))        #打印name
        #判断语句，根据传入参数打印指定结果
        if self.name == 'WYZ':      #传入WYZ，打印 于是童姥说：师弟！
            print("于是童姥说：师弟！")
        elif self.name == '李秋水':        #传入李秋水，打印 于是童姥说：呸，贱人！！！
            print("于是童姥说：呸，贱人！！！")
        elif self.name == '丁春秋':        #传入丁春秋，打印 于是童姥说：叛徒！我杀了你！！！！
            print("于是童姥说：叛徒！我杀了你！！！！")
        else:       #传入其他内容，打印 于是童姥说：是谁？
            print("于是童姥说：是谁？")

        #打印童姥随机获取到的初始属性值
        print("童姥最初属性值为：hp={}、power={}、mp={}".format(self.hp,self.power,self.mp))

    def fight_zms(self):        #定义fight_zms方法（天山折梅手）
        self.hp = self.hp / 2           #调用该方法后，hp值缩减2倍
        self.power = self.power * 10    #调用该方法后，power值提升10倍
        self.mp = self.mp * 3       #调用该方法后，mp值提升3
        #打印调用该方法后童姥的属性值
        print("童姥调用技能后的属性值为：hp={}、power={}、mp={:.2f}".format(self.hp,self.power,self.mp))


    def enemy(self):        #定义enemy敌人方法
        self.enemy_hp = random.choice(hp)           #定义敌人属性——hp血量，使用choice()函数随机返回一个值
        self.enemy_power = random.choice(power2)    # 定义敌人属性——power武力值（攻击力），使用choice()函数随机返回一个值
        #打印敌人属性值
        print("敌人的属性值为：hp={}、power={}".format(self.enemy_hp,self.enemy_power))

    def rule(self,m=0,n=0,z=0):     #定义rule比赛规则（五局三胜制）方法，并初始化变量
        self.m = m      #定义m属性，用于统计童姥赢得比赛的次数
        self.n = n      #定义n属性，用于统计敌人赢得比赛的次数
        self.z = z      #定义z属性，用于判断某一方赢得次数是否为3
        for i in range(5):      #for循环，指定循环次数（最多5次）
            i += 1      #i变量自加，用于判断比赛回合
            print("第{}回合".format(i))    #打印回合次数
            while self.z != 3:      #当z=3（某一方赢3次）时，结束当前循环语句
                self.hp = self.hp - self.enemy_power    #定义当前童姥hp计算公式
                self.enemy_hp = self.enemy_hp - self.power * self.mp    #定义当前敌人hp计算公式
                #输出出招后童姥、敌人的hp，并限定显示俩位数:.2f
                print("打完后，童姥hp={:.2f}、敌人hp={:.2f}".format(self.hp, self.enemy_hp))

                if self.hp < 0:     #如果童姥hp<0，敌人赢，输出童姥输了
                    self.n += 1     #n+1，代表敌人赢一局
                    print("m={}、n={}，这局童姥输了".format(self.m, self.n))
                    if self.n == 3:     #如果敌人已经赢了3局
                        self.z = 3      #返回z=3
                        break       #结束while循环
                    break       #跳出while循环语句，进入下一局比赛（下一次循环）
                elif self.hp == self.enemy_hp == 0:     #如果童姥hp=敌人hp=0，输出平局
                    print("m={}、n={}，这局是平局".format(self.m, self.n))
                    if i == 5:      #如果已经循环了5次，且都是平局
                        self.z = 3  #返回z=3
                        break   #结束while循环
                    break       #跳出while循环语句，进入下一局比赛（下一次循环）
                elif self.enemy_hp < 0:     #如果敌人hp<0，童姥赢，输出童姥赢了
                    self.m += 1             #m+1，代表童姥赢一局
                    print("m={}、n={}，这局童姥赢了".format(self.m, self.n))
                    if self.m == 3:     #如果童姥已经赢了3局
                        self.z = 3      #返回z=3
                        break       #结束while循环
                    break       #跳出while循环语句，进入下一局比赛（下一次循环）

        #如果m=3，输出本次比武童姥获胜，否则输出童姥输了
        if self.m == 3:
            print("本次比武童姥获胜了！！！")
        else:
            print("很遗憾！本次比武童姥输了！")

tl = Tonglao()      #对类进行实例化
tl.see_people('WYZ')        #给see_people方法传参
tl.fight_zms()      #调用Tonglao类下fight_zms()方法
tl.enemy()          #调用Tonglao类下enemy()方法
tl.rule()           #调用Tonglao类下rule()方法
print()