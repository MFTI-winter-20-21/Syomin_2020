a = [[["a"], ["b"]], [["c"], ["d"]]]
count = 0

for i in range(len(a)):
    print("Число i:", i)

    for j in range(len(a[i])):
        print("Длина i-того списка из pointsnap:", len(a[i]))
        print("Число j:", j)
        a[i][j].append(str(count))
        count += 1

print(a)
