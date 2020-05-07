import turtle
t = turtle.Turtle()
t.shape("turtle")


def cCircle(radius):

    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()

    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    t.pendown()


cCircle(150)
cCircle(100)
cCircle(50)


def binary_to_decimal(binary):
    decimal = 0
    n = 1

    for i in range(len(binary)-1, -1, -1):

        decimal = decimal + int(binary[i]) * n
        n = n*2

    return decimal


def decimal_to_binary(decimal):
    decimal = int(decimal)
    binary = ""

    while(True):

        quotient = decimal//2
        rest = decimal % 2
        binary = str(rest)+binary

        if (quotient == 0):
            break

        decimal = quotient

    return binary


d = input("10진수:")
print(decimal_to_binary(d))
b = input("2진수:")
print(binary_to_decimal(b))
