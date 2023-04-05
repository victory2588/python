def drop(a,n=1):   # 슬라이싱 이용
    return a[n:]

print(drop([1,2,3],0))
print(drop([1,2,3]))
print(drop([1,2,3],2))
print(drop([1,2,3],5))