#项目分析
'''
构成
- 蛇 Snake
- 食物 Foob
- 世界 World
- 蛇和食物属于这个世界
- 思路分析
    - 食物是一种独立的食物
    - 蛇也可以认为是一个独立的事物
    - 世界也是，但是世界负责显示
'''
import tkinter,random

class Foob():
    '''
    功能：
        1.出现在图画的每一个地方
        2. 一旦被吃，则增加蛇的分数
    '''
    def __init__(self,queue):
        '''
        自动产生一个食物
        '''
        self.new_food()
        self.queue=queue
    def new_food(self):
        '''
        功能：产生一个食物
        产生一个食物随机出现的坐标
        '''
        x= random.randrange(50,480,10)
        y= random.randrange(50,480,10)
        self.position = x,y#position存放食物

        #队列，就是一个不能访问内部元素，只能从头弹出第一个元素并只能在队尾的list
        #把一个食物产生的消息放到队里
        # 我的定义是 : 消息是一个dict,k代表消息类型，v代表数据
        self.queue.put({"foob":self.position})
class Snake():
    '''
    蛇的功能：
        1.蛇能动，由我们的上下左右控制
        2.蛇能动，都需要重新计算舌头的位置
        3.检测游戏是否结束
    '''
    def move(self):
        '''
        负责蛇的移动
            1.重新计算舌头的坐标
            2.蛇头和食物相遇，则加分，重新生成食物，通知world，加分
            3.否则，蛇能动
        :return:
        '''
        nwe_snake_point=self.cal_new_pos()#重新计算蛇头的位置
        # 蛇头的位置和食物的位置相同
        if self.foob.position == nwe_snake_point:
            self.points_earned += 1
            self.queue.put({"points_earned":self.points_eaened})
            self.food.new_food()
        elif:

