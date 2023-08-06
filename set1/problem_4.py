from math import floor

list = [10, 20, 30, 40]

sum=0
avg=0

for i in list:
  sum+=i

avg=sum/len(list)
print("Sum of List:",sum)
print ("Average of List:",floor(avg))