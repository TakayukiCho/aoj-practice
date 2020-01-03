def insertion_sort(ls):
  for standard_i in range(1, len(ls)):
    standard_val = ls[standard_i]
    compared_i = standard_i - 1
    while compared_i >= 0 and ls[compared_i] > standard_val:
      ls[compared_i+1] = ls[compared_i]
      compared_i -= 1
    ls[compared_i+1] = standard_val
  return ls

listing = [9,2,3,1,5,3,5,7,8,3]
print(f"before sort: {listing}")
sorted_ls = insertion_sort(listing)
print(f"after sort: {sorted_ls}")