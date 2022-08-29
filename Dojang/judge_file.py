with open('words.txt','r') as file:
    words=file.readline().split(' ')
    for i in words:
        if 'c' in i:
            print(i.strip(',.'))