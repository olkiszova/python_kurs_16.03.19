def selectionSort(alist):
    for i in range(len(alist)):

        # Find the minimum element in remaining
        index_min_wart = i

        for j in range(i, len(alist)):
            if alist[index_min_wart] > alist[j]:
                index_min_wart = j

        # Zamiana nowego minimum ze starym minimum

        alist[i], alist[index_min_wart] = alist[index_min_wart], alist[i]

    return alist

print(selectionSort([9,1,6,8,4,3,2,0]))