'''
本源码来自公众号菜鸟学Python的小号菜鸟编程大本营
目前菜鸟学Python已经累计全网有30万粉丝，超过400个趣味Python案例
欢迎小伙伴关注，一起来学编程！
'''

import turtle as t

t.title("苦涩")

t.pensize(5)
t.speed(10)
#脸
t.pencolor("orange")
t.begin_fill()
t.penup()
t.goto(0,-200)
t.pendown()
t.fillcolor("Yellow1")
t.circle(200)
t.end_fill()

#嘴

t.pencolor("brown")
t.penup()
t.goto(-70,-70)
t.pendown()
t.right(30)
t.circle(100,60)



#左眼
t.penup()
t.seth(180)
t.goto(-50,20)
t.pendown()
t.begin_fill()
t.fd(100)
t.circle(-10,90)
t.fd(40)
t.circle(-10,90)
t.fd(100)
t.circle(-10,90)
t.fd(40)
t.circle(-10,90)
t.fillcolor("white")
t.end_fill()

t.penup()
t.goto(-80,50)
t.pendown()
t.seth(270)
t.pencolor("black")
t.begin_fill()
t.circle(-20, 360)
t.fillcolor("black")
t.end_fill()


#右眼
t.pencolor("brown")

t.penup()
t.seth(0)
t.goto(30,20)
t.pendown()
t.begin_fill()
t.fd(100)
t.circle(10,90)
t.fd(40)
t.circle(10,90)
t.fd(100)
t.circle(10,90)
t.fd(40)
t.circle(10,90)
t.fillcolor("white")
t.end_fill()

t.penup()
t.goto(60,50)
t.pendown()
t.seth(270)
t.pencolor("black")
t.begin_fill()
t.circle(20, 360)
t.fillcolor("black")
t.end_fill()
#左眼眼泪
t.pencolor("#7EB0C8")
t.penup()
t.goto(-90, 20)  # 找准眼泪位于眼睛的相对位置
t.pendown()
t.seth(270)     # 改变方向向下
t.begin_fill()
t.fd(180)      # 画长度为180的线段
t.right(90)
t.fd(30)
t.right(90)    # 向右调整方向
t.seth(90)
t.fd(180)
t.fillcolor("#7EB0C8")  # 填充颜色的颜色
t.end_fill()


#右眼眼泪
t.penup()
t.goto(70, 20)
t.pendown()

t.seth(270)
t.begin_fill()
t.fd(180)
t.left(90)
t.fd(30)
t.left(90)
t.fd(180)
t.fillcolor("#7EB0C8")
t.end_fill()














t.done()