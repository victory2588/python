def compact(a):
    return list(filter(None,a))

x=[0,1,False,2,'',3,'a','s',34]  # 0,False,'' -> None 값
print(compact(x))