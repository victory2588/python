import turtle as t

n,line=map(int,input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.fd(line)
    t.right(180 - 360 / n)
    t.fd(line)
    t.right(360/n)