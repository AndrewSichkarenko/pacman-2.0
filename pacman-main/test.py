a = list(map(int, input('Enter:').split()))
for i in range(len(a) - 1):
    min_index = i
    min_value = a[i]
    for j in range(i+1,len(a)):
        if a[j] < min_value:
            min_value = a[j]
            min_index = j
    a[min_index] = a[i]
    a[i] = min_value
print(a)