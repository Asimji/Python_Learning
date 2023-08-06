list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list=[]

for i in range(len(list1)):
  list.append(list1[i]+list2[i])

print(list)