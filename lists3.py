list_holder = ["hi", "bye"]
list_holder1 = ["hello", "goodbye"]
list_holder.append(list_holder1)
print(list_holder)
print("    ")


list1 = ["hi", "hello"]
list2 = ["goodbye", "adios"]
list3 = [list1, list2]
for x in list3:
    print(x)
print("    ")


list_1 = [2, 3, 7]
list_2 = [5, 12, 4]
list_3 = [8, 0, 9]
list_4 = [list_1, list_2, list_3]

sum = 0

for x in list_4:
    sum += x[0]
print(sum)
print("    ")

sum1 = 0
for x in list_4[0]:
    sum1 += x
print(sum1)





