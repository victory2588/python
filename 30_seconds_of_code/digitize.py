def digitize(n):
    return list(map(int,str(n)))  # map의 반환값은 map 객체이기 때문에 list로 변환
                                    # str(n)을 하는 이유는, str로 변환해야 각각의 요소에 접근할 수 있어서(?)
print(digitize(4234))