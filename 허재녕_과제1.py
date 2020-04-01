import turtle
t = turtle.Turtle()
t.shape('turtle')
t.shapesize(2,2,3)
size = 200
tri_angle = 120


t.left(tri_angle/2)
t.forward(size)
t.left(tri_angle)
t.forward(size)
t.left(tri_angle)
t.forward(2*size)
t.right(tri_angle)
t.forward(size)
t.right(tri_angle)
t.forward(size)