import turtle
#과제1#
name_first = input("이름 첫째자는")
name_second = input("이름 둘째자는")
name_third = input("이름 셋째자는")
name_length = len(name_first)+len(name_second)+len(name_third)
changed_name_first = ""
changed_name_second = ""
changed_name_third = ""
if(ord(name_first[0])<ord('a')):
    changed_name_first += chr(ord(name_first[0])+32)
else:
    changed_name_first += name_first[0]

if(ord(name_second[0])<ord('a')):
    changed_name_second += chr(ord(name_second[0])+32)
else:
    changed_name_second += name_second[0]

if(ord(name_third[0])<ord('a')):
    changed_name_third += chr(ord(name_third[0])+32)
else:
    changed_name_third += name_third[0]

changed_name_first += name_first[1:]
print("*"*name_length)
print(changed_name_second+changed_name_third+changed_name_first)
#과제2#
t = turtle.Turtle()
side_len = 50
angle_third  = 60

t.left(angle_third)
t.forward(side_len)
t.right(angle_third)
t.forward(side_len)
t.right(angle_third)
t.forward(side_len)
t.right(angle_third)
t.forward(side_len)
t.right(angle_third)
t.forward(side_len)
t.right(angle_third)
t.forward(side_len)


t.penup()
t.goto(side_len/2,0)
t.pendown()
t.color('red')
t.write("stop")



