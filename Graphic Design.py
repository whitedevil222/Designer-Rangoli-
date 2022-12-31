from turtle import*
bgcolor('black')
tracer(100)
c = ['black', 'white', 'black', 'white', 'black', 'white']
for i in range(700):
    color(c[i%6])
    fd(7)
    lt(88)
    fd(i*3)
    circle(10)
    lt(59)
done()