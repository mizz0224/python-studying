import turtle
#2-1과제20153287 허재녕#
number = int(input("세자리 정수 입력 "))

hun_num = number//100
ten_num = (number-hun_num*100)//10
one_num = number%10
fin_num = one_num*100+ten_num*10+hun_num
print("입력한 수의 역순",fin_num)
# 공통과제 20153287허재녕#
t = turtle.Turtle()
length = int(input("변의 길이를 입력해주세용"))


t.shape('arrow')

half = length/2
rightangle = 90

t.circle(half)
t.penup()
t.forward(half)
t.pendown()



t.left(rightangle)
t.forward(length)

t.left(rightangle)
t.forward(length)

t.left(rightangle)
t.forward(length)

t.left(rightangle)
t.forward(length)

