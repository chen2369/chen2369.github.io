total = int(input())
for i in range(total):
    num = int(input())
    linetotal = []
    for j in range(num):
        line = [int(l) for l in input().split()]
        linetotal.extend(list(range(line[0], line[1])))
    
    print(len(set(linetotal)))