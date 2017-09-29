def is_fibonacci(lst):
    a = lst

    for i in range(0,len(a)-2):
        if a[i+2] == a[i] + a[i+1]:
            continue
        else:
            return False



b = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
c = is_fibonacci(b)
if c == False:
    print("This list is not fibonacci")
else:
    print("fibonacci")

