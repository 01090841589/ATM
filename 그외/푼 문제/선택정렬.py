def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

data = [123, 21346, 3145, 13246, 24567, 2134, 267]
selectionsort(data)
print(data)