'''
本源码来自公众号菜鸟学Python的小号菜鸟编程大本营
目前菜鸟学Python已经累计全网有30万粉丝，超过400个趣味Python案例
欢迎小伙伴关注，一起来学编程！
'''

import turtle as t

t.pensize(5)
t.speed(10)
#脸
t.pencolor("orange")  # 画笔的颜色变为橘色
t.begin_fill()  # 准备开始填充
t.penup()
t.goto(0,-200)
t.pendown()
t.fillcolor("Yellow1")
t.circle(200)     # 画一个半径为200的圆，并填充为黄色
t.end_fill()
# #嘴
t.pencolor("brown")  # 将画笔的颜色改为棕色
t.penup()
t.goto(-30, -20)    # 画笔跳转到(-30，-20)的位置，然后画一条长度为60的直线
t.pendown()
t.fd(60)



# #眼睛
t.penup()
t.seth(0)
t.pensize(3)

#  #右眼
t.goto(70,20)
t.pendown()
t.begin_fill()
t.fd(100)       # 通过不断画直线和四分之一圆来画出一个圆角矩形的眼睛
t.circle(10,90)
t.fd(20)
t.circle(10,90)
t.fd(100)
t.circle(10,90)
t.fd(20)
t.circle(10,90)
t.fillcolor("white")  # 将眼睛填充为白色
t.end_fill()
#眼瞳
t.penup()     # 跳转画笔，准备画眼瞳
t.goto(80,60)
t.pendown()
t.seth(270)   # 由于眼瞳是半圆，所以注意要调整画笔的角度
t.begin_fill()
t.circle(30, 180)  # 画一个半径为30的半圆
t.fillcolor("black")  # 填充为黑色
t.end_fill()

#左眼
t.penup()
t.seth(180)
t.goto(-70,20)
t.pendown()
t.begin_fill()
t.fd(100)
t.circle(-10,90)
t.fd(20)
t.circle(-10,90)
t.fd(100)
t.circle(-10,90)
t.fd(20)
t.circle(-10,90)
t.fillcolor("white")
t.end_fill()

t.penup()
t.goto(-80,60)
t.pendown()
t.seth(270)
t.begin_fill()
t.circle(-30, 180)
t.fillcolor("black")
t.end_fill()
t.done()

