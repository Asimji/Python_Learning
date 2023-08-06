input=[64, 25, 12, 22, 11]

for i in range(len(input)):
    min=i
    for j in range(i+1,len(input)):
      if(input[j]<input[min]):
         min=j
    temp=input[i]
    input[i]=input[min]
    input[min]=temp
   

print(input)
