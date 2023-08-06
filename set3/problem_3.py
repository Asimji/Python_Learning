Input,target= [2, 7, 11, 15],9


i,j=0,len(Input)-1
while (j>i):
  if(Input[i]+Input[j]==target):
    print(i,j)
    i=i+1
    j=j-1
  if(Input[i]+Input[j]<target):
    i=i+1;
  if(Input[i]+Input[j]>target):
    j=j-1; 


 