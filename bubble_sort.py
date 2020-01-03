def bubble_sort(ls):
  length = len(ls)
  for end in range(length):
    for cmp_1_i in range(length-2, end-1, -1):
      cmp_2_i = cmp_1_i + 1
      if ls[cmp_1_i] > ls[cmp_2_i]:
        tmp = ls[cmp_1_i]
        ls[cmp_1_i] = ls[cmp_2_i]
        ls[cmp_2_i] = tmp
  return ls

unsorted = [3,2,3,5,6,7,8,1,3,5,7,1,3,5]
print(f"unsorted: {unsorted}")

sorted = bubble_sort(unsorted)
print(f"sorted: {sorted}")