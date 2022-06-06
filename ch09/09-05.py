import turtle as t
t.shape('turtle')

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.pencolor('blue')
for _ in range(4):
    t.left(90)
    t.forward(150)

t.pencolor('green')
t.goto(100, -100)
t.goto(-100, -100)
t.home()