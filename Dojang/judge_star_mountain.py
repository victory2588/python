a=int(input())
for i in reversed(range(a)):
    for j in range(a):
        if i<=j:
            print('*',end='')
        else:
            print(' ',end='')
    a += 1
    if a > 2 * a - 1:
        break
    print()


