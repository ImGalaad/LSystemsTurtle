from turtle import *

alphabet = {"F", "S", "+", "-", "[", "]"}

t = Turtle()

t.color("maroon")
t.fillcolor("green")
t.ht()


def leaf(length):
    print("L", end=" ")
    t.color("green")
    t.width(0)
    t.left(120)
    t.begin_fill()
    for i in [length, length * 2, length, length, length * 2, length]:
        t.right(360 / 6)
        t.forward(i)
    t.end_fill()
    t.color("maroon")
    t.right(120)


def system(rules, ntime, length, angle=20, stack=[]):
    if ntime != 0:
        for item in rules:
            print(item, end=" ")

            if item == "F":
                t.width(length**0.4)
                t.forward(length)
                system(rules, ntime - 1, length * 0.4, angle, stack)

            elif item == "S":
                t.width(length**0.4)
                t.forward(length)

            elif item == "+":
                t.left(angle)

            elif item == "-":
                t.right(angle)

            elif item == "[":
                stack.append([t.pos()[0], t.pos()[1], t.heading()])

            elif item == "]":
                position = stack.pop()
                t.penup()
                t.goto(position[0], position[1])
                t.setheading(position[2])
                t.pendown()

        system(rules, ntime - 1, length * 0.8, angle, stack)

    else:
        leaf((length * 4) ** 0.5)


t.speed(0)
t.penup()
t.goto(0, -300)
t.pendown()

# t.left(90)
# rules = 'S[++++S--F]S-[----S++F]S+' # Tree
# system(rules, 3, 30, 7)

t.left(100)
rules = "S-S[---S+F+F]S+[+S-F--F]F+[+S-F--F]-"  # Tree 2
system(rules, 3, 40, 25)

# t.clear()

exitonclick()
