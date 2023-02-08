def second_index(text,symbol):
    if text.count(symbol)<2:  # 그 symbol이 2개 이상 있는지부터 확인
        return None

    first=text.find(symbol)  # 일단 첫번째 심볼이 있는 곳을 찾고
    return text.find(symbol,first+1)  # 시작 지점을 그 심볼 다음으로 옮기기

print(second_index("hi","i"))

# 선행지식: count와 find 메소드가 있다는 것 알기