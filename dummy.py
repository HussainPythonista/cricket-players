# # Sample data structure
# data = [
#     [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}],
#     [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}],
#     [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]
# ]

# # Buckets to store popped values
# bucket1 = []
# bucket2 = []
# bucket3 = []

# # Pop value from the first list and delete the corresponding record from the other two lists
# popped_value = data[0].pop(0)
# for lst in data[1:]:
#     for i, item in enumerate(lst):
#         if item['id'] == popped_value['id']:
#             del lst[i]
#             break

# # Place the popped value into the buckets
# bucket1.append(popped_value)
# bucket2.append(popped_value)
# bucket3.append(popped_value)
# # "Updated Data:")
# # print(data)
# # print("Bucket 1:", bucket1)
# # print("Bucket 2:", bucket2)
# # print("Bucket 3:", bucket3)

# # print(

print(66//11)