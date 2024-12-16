from collections import Counter
my_list = [1,1,1,2,2,3,3,3,3,3]
count_list = Counter(my_list)

most_common = count_list.most_common(2)

print(count_list)
# print(count_list.most_common())
# print(count_list.most_common(2))

keys_in_most_common = []

for item in most_common:
    keys_in_most_common.append(item[0])

print(keys_in_most_common)
