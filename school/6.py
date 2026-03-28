# fd() - вперед
# bk() - назад
# lt() - влево
# rt() - вправо
# up() - поднять хвост
# down() - опустить хвост
# tracer(0) - отключить анимации
# done() - оставить окно
# screensize(xxxx, yyyy) - размер окна
# goto(x, y) - перейти к точке, dot(5, 'rad') - поставить точку

# Посчитать кол-во отрезков - 360 / x градусов
# Сделать маштаб побольше и посмотреть экстримально близкие точки
# Если прямоугольник 2*3, то точек 3*4
# Разбивать фигуры на простые

# from turtle import *
# tracer(0)
# m = 50
# screensize(2000, 2000)
# lt(90)

# ... - изменяемая часть

# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*m, y*m)
#         dot(5, 'red')
# done()





from turtle import *
tracer(0)
screensize(2000, 2000)
lt(90)
m = 50

for i in range(5):
    goto(xcor() + 5*m, ycor() + 4*m)
    goto(xcor() + 4*m, ycor() - 4*m)
    goto(xcor() - 7*m, ycor() - 2*m)
    goto(xcor() - 2*m, ycor() + 2*m)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'red')
done()