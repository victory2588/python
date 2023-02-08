def between_markers(text,begin,end):
    if begin in text:
        begin_index=text.find(begin)+len(begin)  # 시작 마커 다음의 문자부터 출력해야하니까 len(begin)을 더해줌
    else:
        begin_index=0

    if end in text:
        end_index=text.find(end)
    else:
        end_index=len(text)

    return text[begin_index:end_index]

print(between_markers('What is >apple<','>','<'))
print(between_markers("<head><title>My new site</title></head>","<title>","</title>"))

