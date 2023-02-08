a,b=map(int,input('').split())
for i in range(a,b+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%7==0:
        print('Buzz')
    elif i%5==0:
        print('Fizz')
    else:
        print(i)
'''
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
--> 이렇게 짧게 줄일 수 있음! 근데 다른 사람이 보고 어려울 정도로 줄이면 안됨..
'''