a = int(input())
b = list('')
for num in range(2, a):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            b.append(num)
for i in b[i]:
    print(b[i+1])