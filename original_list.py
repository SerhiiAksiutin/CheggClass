original_list = [4, 13, 17, 20, 24, 31, 32, 55, 100]

even_nums = []
odd_nums = []
for v in original_list:
    x = v % 2
    if x == 0:
        even_nums.append(v)
    else:
        odd_nums.append(v)

print('The even numbers are: %s.\nThe odd numbers are: %s.' % (
  str(even_nums).strip('[]'), str(odd_nums).strip('[]')))
