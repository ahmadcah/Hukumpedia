target = input("keyword: ")
with open("temp.txt", encoding='utf8') as openfile:
    for line in openfile:
        for part in line.split():
            if target in part:
                print(line)
