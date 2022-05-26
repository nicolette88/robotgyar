import turtle as t

t.shape('turtle')


def teglalap(vizszintes, fuggoleges, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for szamlalo in range(1, 3):
        t.forward(vizszintes)
        t.right(90)
        t.forward(fuggoleges)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')


# cipő
t.penup()
t.goto(-100, -150)
teglalap(50, 20, 'Navy')
t.goto(-30, -150)
teglalap(50, 20, 'Navy')

# lábak
t.goto(-25, -50)
teglalap(15, 100, 'Lemon Chiffon')
t.goto(-55, -50)
teglalap(-15, 100, 'Lemon Chiffon')

# test
t.goto(-90, 100)
teglalap(100, 150, 'Deep Pink')

# karok
t.goto(-150, 70)
teglalap(60, 15, 'Misty Rose')
t.goto(-150, 110)
teglalap(15, 40, 'Misty Rose')
t.goto(10, 70)
teglalap(60, 15, 'Misty Rose')
t.goto(55, 110)
teglalap(15, 40, 'Misty Rose')

# nyak
t.goto(-50, 120)
teglalap(15, 20, 'grey')

# fej
t.goto(-85, 170)
teglalap(80, 50, 'Peach Puff')

# szemek
t.goto(-60, 160)
teglalap(30, 10, 'white')
t.goto(-55, 155)
teglalap(5, 5, 'black')
t.goto(-40, 155)
teglalap(5, 5, 'black')

# száj
t.goto(-65, 135)
teglalap(40, 5, 'black')

t.hideturtle()