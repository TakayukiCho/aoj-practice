def selection_sort(ls):
    length = len(ls)
    for i in range(length):
       min_i = i 
       for j in range(i+1, length):
         if ls[j] < ls[min_i]:
           min_i = j 
       tmp = ls[i]
       ls[i] = ls[min_i]
       ls[min_i] = tmp 
    return ls

ls = [3,4,2,2,6,4,3,5,6,7,7,1,2,6,2]
sorted = selection_sort(ls)
print(sorted)